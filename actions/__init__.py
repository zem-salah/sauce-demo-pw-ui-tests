import os
import inspect
import importlib


def init_actions_module(page):
    """
    This method dynamically initialize action classes and add them
    in behave context object. Each action class is accessible in other
    parts of the project (should be steps) via context.<class_name>
    in order to use action methods in those classes.

    Example :
        context.Login.login_as(user)

    Args:
        page: playwright Page instance.
    """
    actions_path = os.path.dirname(os.path.abspath(__file__))
    module_name = os.path.basename(actions_path)

    for filename in os.listdir(actions_path):
        if filename.endswith('.py') and filename != '__init__.py':
            module = importlib.import_module(
                f"{module_name}.{filename[:-3]}")
            for name, obj in inspect.getmembers(module, inspect.isclass):
                # If the class has a 'should_init' attribute set to True
                if hasattr(obj, 'should_init') and obj.should_init \
                        and hasattr(obj, 'set_page'):
                    obj.set_page(page)
