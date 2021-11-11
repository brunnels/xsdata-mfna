import importlib
import inspect
import logging
import os
import sys
from dataclasses import is_dataclass
from importlib.machinery import SourceFileLoader
from importlib.util import spec_from_file_location

logger = logging.getLogger(__name__)
logging.basicConfig(stream=sys.stdout, level=logging.DEBUG)

mfna_dir = os.path.abspath(os.path.join(os.getcwd(), 'mfna_full'))
module_base = "mfna_full"

modules = []

with os.scandir(mfna_dir) as itr:
    for entry in itr:
        if entry.name.endswith("_input.py") and entry.is_file():
            module_name = str(entry.name).rpartition("_")[0]
            modules.append(module_name)

for module_name in modules:
    init_cleanup = []
    module_directory = os.path.join(mfna_dir, module_name)

    if not os.path.exists(module_directory):
        logger.info(f"creating module directory {module_directory}")
        os.makedirs(module_directory)
        module_files = [
            f"{module_name}.py",
            f"{module_name}_input_parms.py",
            f"{module_name}_request.py",
            f"{module_name}_input.py",
            f"{module_name}_output.py",
            f"{module_name}_response.py",
        ]
        class_names = []
        init_out_file = os.path.join(module_directory, f"__{module_name}__init__.py")
        with open(init_out_file, "w+") as init_file:
            for module_file in module_files:
                module_filename = os.path.join(mfna_dir, module_file)
                file_import = module_file.partition(".")[0]
                mn = f"{module_base}.{file_import.replace('-', '_')}"

                # need to handle reserved keyword modules that have mod appended to their filenames
                if module_file == f"{module_name}.py" and not os.path.exists(module_filename):
                    module_filename = os.path.join(mfna_dir, f"{file_import}_mod.py")
                    file_import = f"{file_import}_mod.py"

                loader = SourceFileLoader(mn, module_filename)
                spec = importlib.util.spec_from_loader(mn, loader)
                loaded_module = importlib.util.module_from_spec(spec)
                loader.exec_module(loaded_module)

                for name, obj in inspect.getmembers(loaded_module, inspect.isclass):
                    if obj.__module__ == loaded_module.__name__ \
                            and (is_dataclass(obj) or module_file == f"{module_name}.py"):
                        class_names.append(name)
                        imp_str = f"from .{file_import} import {name}\n"
                        init_cleanup.append(imp_str)
                        init_file.write(imp_str)

                logger.info(f"moving file {module_file} into module directory {module_directory}")
                os.rename(module_filename, os.path.join(module_directory, module_file))

            init_file.write("\n__all__ = [\n")
            for class_name in list(dict.fromkeys(class_names)):
                all_str = f'    "{class_name}",\n'
                init_cleanup.append(all_str)
                init_file.write(all_str)
            init_file.write("]\n")

        os.rename(init_out_file, os.path.join(module_directory, "__init__.py"))

        infile = os.path.join(mfna_dir, "__init__.py")
        outfile = os.path.join(mfna_dir, "__clean_init.py")
        with open(infile) as fin, open(outfile, "w+") as fout:
            for line in fin:
                for word in init_cleanup:
                    newline = line.replace(word, "")
                    if newline != line:
                        break
                fout.write(newline)

        os.unlink(infile)
        os.rename(outfile, infile)

global_module_imports = []
with os.scandir(mfna_dir) as itr:
    for entry in itr:
        if entry.is_file() and entry.name != "__init__.py":
            global_module_imports.append(f"from .{str(entry.name).rpartition('.')[0]}")

for module_name in modules:
    module_directory = os.path.join(mfna_dir, module_name)

    if os.path.exists(module_directory):
        logger.info(f"fixing global module import in directory {module_directory}")
        with os.scandir(module_directory) as itr:
            for entry in itr:
                if entry.is_file() and entry.name != "__init__.py":
                    infile = entry.path
                    outfile = f"{entry.path}__clean"
                    with open(infile) as fin, open(outfile, "w+") as fout:
                        for line in fin:
                            for word in global_module_imports:
                                newline = line.replace(word, word.replace("from .", "from .."))
                                if newline != line:
                                    break
                            fout.write(newline)

                    os.unlink(infile)
                    os.rename(outfile, infile)
