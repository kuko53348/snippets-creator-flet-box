import json
from FletBox.FletBox_snippets_creator.FletBox_create_attributes_widgets import (
    attrs_all_placeholders_complete,
)
from FletBox.FletBox_snippets_creator.FletBox_create_widgets import (
    only_controls,
)
from FletBox.FletBox_snippets_creator.FletBox_create_modules_widgets import (
    only_modules,
)


class make_snippet:
    """
    ### Make snnipets
     - Make snippets from vscode to nvim
     - just copy and paste
     - delete, update, create
     - show all keys

    ```FletBox
    nombre = 'module scallfold let'
    prefijo = 'module.scallfold.init'
    description = f'Make a nombre {prefijo}'
    texto ="""

    """
    instance = make_snippet(path='./FletBox', figtle_name='FletBox.json')
    ```

    ### READ ALL DATA
    ```FletBox
    check_value = instance.read_json()
    print(check_value)
    ```

    ### GET ALL KEYS
    ```FletBox
    check_keys = instance.get_current_keys()
    print(check_keys)
    ```

    ### READ ALL DATA
    ```FletBox
    check_value = instance.read_json(
        name=nombre, prefix=prefijo, data=texto, description=description
    )
    print(check_value)
    ```

    ### UPDATE ALL DATA
    ```FletBox
    check_value = instance.update_json(
           name=nombre,
           prefix=prefijo,
           data=texto,
           description=description
       )
    print(check_value)
    ```

    ### DELETE DATA FROM JSON
    ```FletBox
    checking = instance.delete_json(snippet_name=nombre)
    print(checking)
    ```

    ```
    """

    def __init__(
        self, path: str = "./FletBox", file_name: str = "FletBox.json"
    ):
        self.path = path
        self.file_name = file_name
        self.full_path = f"{path}/{file_name}"
        # self.old_data = self.read_json()
        self.tmp_dict = dict()

    def check_value(self):
        with open(self.full_path, "r", encoding="utf-8") as file:
            return file.read()

    def read_json(self, load_dict: bool = False):
        with open(self.full_path, "r", encoding="utf-8") as file:
            if self.check_value() == "":
                return {}
            # return file.read().keys()
            if load_dict:
                return file
            return json.load(file)

    def get_current_keys(self):
        check_value = self.read_json()
        return check_value.keys()

    def update_json(
        self,
        name: str = "",
        prefix: str = "",
        data: str = "",
        description: str = "",
        debug=False,
    ):
        check_value = self.read_json()
        check_key = check_value.get(name, False)

        if check_key:
            # check_value[name]=name
            check_value[name]["prefix"] = prefix
            check_value[name]["body"] = data.splitlines()
            check_value[name]["description"] = description
            with open(self.full_path, "w", encoding="utf-8") as file:
                json.dump(check_value, file, indent=2)
                print(f"\nSnippet [{name}] was update!!!")
                return True
        print(f"\nSnippet [{name}] Not exits exist!!!")
        return False

    def delete_json(self, snippet_name: str = ""):
        check_value = self.read_json()
        check_key = check_value.get(snippet_name, False)

        if check_key:
            del check_value[snippet_name]
            with open(self.full_path, "w", encoding="utf-8") as file:
                json.dump(check_value, file, indent=2)
                print(f"\nSnippet [{snippet_name}] was erase!!!")
                return True

        print(f"\nSnippet [{snippet_name}] Not exits exist!!!")
        return False

    def read_original_to_write_json(
        self,
        name: str = "",
        prefix: str = "",
        data: str = "",
        description: str = "",
        debug=False,
    ):
        tmp_dict = self.tmp_dict
        snippet = {
            name: {
                "prefix": prefix,
                "description": f"Make a {name} widget",
                "body": data.splitlines(),
            }
        }
        # print(self.old_data)

        # tmp_dict.update(self.old_data)
        tmp_dict.update(snippet)

        if debug:
            print(json.dumps(tmp_dict, indent=1))

        return tmp_dict

    def write_json(self, data_to_write: dict = {}, tag_name: str = "tag-name"):
        # print(json.dumps(snippet, indent=1))

        with open(self.full_path, "w", encoding="utf-8") as file:
            json.dump(data_to_write, file, indent=2)

        print(f"[*] - SNIPPET WAS CREATE {tag_name} FletBox.json")


if __name__ == "__main__":
    # ===============================================================
    # Ejemplo de uso
    # nombre = "Scaffold structure module init"
    # prefijo = "module.scaffold.init"
    # description = f"Make a {prefijo}"
    #
    # texto = """
    # """
    # instance = make_snippet(path="./FletBox", file_name="FletBox_widgets_FletBox.json")

    # READ ALL DATA
    # check_value = instance.read_json()
    # print(check_value)

    # GET ALL KEYS
    # check_keys = instance.get_current_keys()
    # print(check_keys)

    # WRITE ALL DATA
    # check_value = instance.read_json(
    #     name=nombre, prefix=prefijo, data=texto, description=description
    # )
    # print(check_value)

    # UPDATE ALL DATA
    # check_value = instance.update_json(
    #        name=nombre,
    #        prefix=prefijo,
    #        data=texto,
    #        description=description
    #    )
    # print(check_value)

    # DELETE DATA FROM JSON
    # checking = instance.delete_json(snippet_name=nombre)
    # print(checking)

    # ==================== CREATE ATTRIBUTES WIDGETS ======================
    instance = make_snippet(
        path="./FletBox/", file_name="FletBox_attribute_widgets.json"
    )
    check_value={}
    # print(attrs_all_placeholders_complete)
    # MAKE SNIPPETS FROM DICT
    # FletBox.FletBox_SNIPPETS_CREATOR.FletBox_CREATE_ATTRIBUTES_WIDGETS IMPORT
    for index, value in attrs_all_placeholders_complete.items():
        name = f"FletBox widgets {index}"
        prefix = f"{index}"
        description = f"widget {index.replace('_', ' ')}"
        check_value = instance.read_original_to_write_json(
            name=name,
            prefix=prefix,
            data=value,
            description=description,
        )
        # print(check_value)
    old_data = instance.read_original_to_write_json()
    # REMOVE EMPTY KEY=""
    del old_data[""]
    old_data.update(check_value)
    instance.write_json(data_to_write=old_data, tag_name="FletBox-attributes")

    # ==================== CREATE WIDGETS WIDGETS ======================

    instance = make_snippet(path="./FletBox/", file_name="FletBox_widgets.json")
    # print(attrs_all_placeholders_complete)
    # MAKE SNIPPETS FROM DICT
    # FletBox.FletBox_SNIPPETS_CREATOR.FletBox_CREATE_ATTRIBUTES_WIDGETS IMPORT
    for index, value in only_controls.items():
        name = f"FletBox widgets {index}"
        prefix = f"{index}"
        description = f"widget {index.replace('_', ' ')}"
        check_value = instance.read_original_to_write_json(
            name=name,
            prefix=prefix,
            data=value,
            description=description,
        )
        # print(check_value)
    old_data = instance.read_original_to_write_json()
    # REMOVE EMPTY KEY=""
    del old_data[""]
    old_data.update(check_value)
    instance.write_json(data_to_write=old_data, tag_name="FletBox-widgets")
    # ==================== CREATE WIDGETS MODULES WIDGETS ======================

    instance = make_snippet(
        path="./FletBox/", file_name="FletBox_modules_widgets.json"
    )
    # print(attrs_all_placeholders_complete)
    # MAKE SNIPPETS FROM DICT
    # FletBox.FletBox_SNIPPETS_CREATOR.FletBox_CREATE_ATTRIBUTES_WIDGETS IMPORT
    for index, value in only_modules.items():
        name = f"FletBox modules widgets {index}"
        prefix = f"{index}"
        description = f"widget {index.replace('_', ' ')}"
        check_value = instance.read_original_to_write_json(
            name=name,
            prefix=prefix,
            data=value,
            description=description,
        )
        # print(check_value)
    old_data = instance.read_original_to_write_json()
    # REMOVE EMPTY KEY=""
    del old_data[""]
    old_data.update(check_value)
    instance.write_json(data_to_write=old_data, tag_name="FletBox-modules-widgets")
    # # ==================== DUMP ALL IN FletBox.json=====================

    # ATTRIBUTES
    instance_attributes = make_snippet(
        path="./FletBox/",
        file_name="FletBox_attribute_widgets.json",
    )
    # WIDGETS
    instance_widgets = make_snippet(
        path="./FletBox/",
        file_name="FletBox_widgets.json",
    )
    # MODULES
    instance_modules_widgets = make_snippet(
        path="./FletBox/",
        file_name="FletBox_modules_widgets.json",
    )

    # WIDGETS in FletBox.js FINAL
    instance_final_widgets = make_snippet(
        path="./FletBox/",
        file_name="FletBox.json",
    )
    attr_data = instance_attributes.read_json()
    widget_data = instance_widgets.read_json()
    module_widget_data = instance_modules_widgets.read_json()
    final_data = instance_final_widgets.read_json()

    all_data = {}
    all_data.update(final_data)
    all_data.update(attr_data)
    all_data.update(module_widget_data)
    all_data.update(widget_data)
    # print(final_data)
    # REMOVE EMPTY KEY=""
    if all_data.get("", False):
        del all_data[""]

    instance_final_widgets.write_json(
        data_to_write=all_data, tag_name="FletBox-all-together"
    )
    # print(all_data)
