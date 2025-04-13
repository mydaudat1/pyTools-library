import ast
import os
from datetime import datetime
from traceback import TracebackException

def cmb_count(file_path=None):
    if file_path is None:
        file_path = os.path.abspath(__file__)
    else:
        file_path = os.path.abspath(file_path)

    if not os.path.isfile(file_path):
        print(f"File not found: {file_path}")
        return

    with open(file_path, "r", encoding="utf-8") as f:
        code = f.read()

    tree = ast.parse(code)

    counts = {
        "if": 0,
        "elif": 0,
        "for": 0,
        "while": 0,
        "def": 0,
        "class": 0,
        "list": 0,
        "dict": 0
    }

    class CountVisitor(ast.NodeVisitor):
        def visit_If(self, node):
            if hasattr(node, 'parent') and isinstance(node.parent, ast.If) and node in node.parent.orelse:
                counts["elif"] += 1
            else:
                counts["if"] += 1
            self.generic_visit(node)

        def visit_For(self, node):
            counts["for"] += 1
            self.generic_visit(node)

        def visit_While(self, node):
            counts["while"] += 1
            self.generic_visit(node)

        def visit_FunctionDef(self, node):
            counts["def"] += 1
            self.generic_visit(node)

        def visit_ClassDef(self, node):
            counts["class"] += 1
            self.generic_visit(node)

        def visit_List(self, node):
            counts["list"] += 1
            self.generic_visit(node)

        def visit_Dict(self, node):
            counts["dict"] += 1
            self.generic_visit(node)

    for node in ast.walk(tree):
        for child in ast.iter_child_nodes(node):
            child.parent = node

    visitor = CountVisitor()
    visitor.visit(tree)

    print(f"\nAnalyzed: {os.path.basename(file_path)}\nResult:")
    for key, value in counts.items():
        if value > 0:
            print(f"{value} '{key}' block{'s' if value > 1 else ''}")

def debug(file_path=None):
    if file_path is None:
        file_path = os.path.abspath(__file__)
    else:
        file_path = os.path.abspath(file_path)

    if not os.path.isfile(file_path):
        print(f"File not found: {file_path}")
        return

    with open(file_path, "r", encoding="utf-8") as f:
        code = f.read()

    tree = ast.parse(code)
    debug_log = []

    class DebugVisitor(ast.NodeVisitor):
        def visit_If(self, node):
            if hasattr(node, 'parent') and isinstance(node.parent, ast.If) and node in node.parent.orelse:
                debug_log.append(f"Found 'elif' at line {node.lineno}")
            else:
                debug_log.append(f"Found 'if' at line {node.lineno}")
            self.generic_visit(node)

        def visit_For(self, node):
            debug_log.append(f"Found 'for' at line {node.lineno}")
            self.generic_visit(node)

        def visit_While(self, node):
            debug_log.append(f"Found 'while' at line {node.lineno}")
            self.generic_visit(node)

        def visit_FunctionDef(self, node):
            debug_log.append(f"Found 'def' at line {node.lineno}")
            self.generic_visit(node)

        def visit_ClassDef(self, node):
            debug_log.append(f"Found 'class' at line {node.lineno}")
            self.generic_visit(node)

        def visit_List(self, node):
            debug_log.append(f"Found 'list' at line {node.lineno}")
            self.generic_visit(node)

        def visit_Dict(self, node):
            debug_log.append(f"Found 'dict' at line {node.lineno}")
            self.generic_visit(node)

    for node in ast.walk(tree):
        for child in ast.iter_child_nodes(node):
            child.parent = node

    visitor = DebugVisitor()
    visitor.visit(tree)

    print(f"\nDebugging: {os.path.basename(file_path)}\n--- DEBUG INFO ---")
    for log in debug_log:
        print(log)

def can_d0(number_one, number_two):
    if number_two == 0:
        return 0
    return number_one / number_two

def help():
    print("This library adds some functions to clean code and debug, sometimes even optimize operators. \n")
    print("Func: cmb_count([file_path])")
    print("   ↳: Helps count command blocks. Optional file_path param for custom file. \n")
    print("Func: debug([file_path])")
    print("   ↳: Debug the program structure by logging elements with line numbers. \n")
    print("Func: can_d0(number 1, number 2)")
    print("   ↳: Helps divide by 0 without error. \n")
    print("Func: note()")
    print("   ↳: Write down some important information. \n")

def note():
    print("NOTE: This library is not written in the latest version of Python.")

def report_err(err, context="Unknown", force_print=True):
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    error_type = type(err).__name__

    if error_type in ["ZeroDivisionError", "IndexError", "KeyError"]:
        level = "WARNING"
    elif error_type in ["TypeError", "AttributeError", "ValueError"]:
        level = "ERROR"
    else:
        level = "CRITICAL"

    header = f"[{timestamp}] [{level}] ({context}) {error_type}: {err}"
    tb_text = ''.join(TracebackException.from_exception(err).format())
    message = f"{header}\nTraceback:\n{tb_text}"

    if force_print:
        print(message, flush=True)

    with open("error_log.txt", "a", encoding="utf-8") as f:
        f.write(message + "\n" + "-" * 60 + "\n")