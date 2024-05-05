bl_info = {
    "name": "Save time",
    "author": "Beketov",
    "version": (1, 0),
    "blender": (4, 0, 2),
    "location": "View3D > N > Custom Addon",
    "description": "Work with many 3d models",
    "warning": "",
    "doc_url": "",
    "category": "Add Mesh",
}



import bpy
import os

# Список файлов .glb в папке и подпапках
file_list = []

# Путь к папке с 3D моделями
models_folder_path = "C:\\3D\\Test\\"

# Переменная для хранения индекса текущего файла
current_file_index = 0

# Определение оператора для загрузки следующего файла из папки
class LoadNextFileOperator(bpy.types.Operator):
    bl_idname = "object.load_next_file"
    bl_label = "Load Next File"
    
    def execute(self, context):
        global current_file_index, file_list
        folder_path = models_folder_path  # Получаем путь к папке из настроек аддона
        
        # Получаем список всех .glb файлов в папке и подпапках, если он еще не был получен
        if not file_list:
            file_list = get_glb_files_in_folder(folder_path)
        
        # Проверяем, есть ли файлы в списке
        if file_list:
            # Загружаем следующий файл из списка
            if current_file_index < len(file_list):
                file_path = file_list[current_file_index]
                bpy.ops.import_scene.gltf(filepath=file_path)  # Импортируем файл .glb
                current_file_index += 1
            else:
                print("No more files to load.")
        else:
            print("No .glb files found in the folder.")
        
        return {'FINISHED'}

# Функция для получения списка всех .glb файлов в указанной папке и подпапках
def get_glb_files_in_folder(folder_path):
    glb_files = []
    for root, dirs, files in os.walk(folder_path):
        for file in files:
            if file.endswith(".glb"):
                glb_files.append(os.path.join(root, file))
    return glb_files

# Определение оператора для перехода на уровень выше
class GoUpLevelOperator(bpy.types.Operator):
    bl_idname = "object.go_up_level"
    bl_label = "Go Up Level"
    
    def execute(self, context):
        global current_file_index, file_list
        # Возвращаемся на уровень выше
        if file_list:
            file_list.clear()  # Очищаем список файлов
            current_file_index = 0  # Сбрасываем индекс файла
        return {'FINISHED'}


# Определение оператора для объединения модели
class ModelJoinOperator(bpy.types.Operator):
    bl_idname = "object.join_model"
    bl_label = "Join Model"

    def execute(self, context):
        # Получаем активный объект (выбранную модель)
        obj = context.active_object
        if obj:
            # Объединяем модель
            bpy.ops.object.join()
        return {'FINISHED'}

# Определение оператора для вращения модели на 90 градусов по оси X
class RotateModelXOperator(bpy.types.Operator):
    bl_idname = "object.rotate_model_x"
    bl_label = "Rotate X"
    
    def execute(self, context):
        # Получаем активный объект (выбранную модель)
        obj = context.active_object
        if obj:
            # Вращаем модель на 90 градусов по оси X
            bpy.ops.transform.rotate(value=1.5708, orient_axis='X', orient_type='GLOBAL', orient_matrix=((1, 0, 0), (0, 1, 0), (0, 0, 1)), orient_matrix_type='GLOBAL', constraint_axis=(True, False, False), mirror=False, use_proportional_edit=False, proportional_edit_falloff='SMOOTH', proportional_size=1, use_proportional_connected=False, use_proportional_projected=False, snap=False, snap_elements={'INCREMENT'}, use_snap_project=False, snap_target='CLOSEST', use_snap_self=True, use_snap_edit=True, use_snap_nonedit=True, use_snap_selectable=False, alt_navigation=True)
  # 90 градусов в радианах
        return {'FINISHED'}

# Определение оператора для вращения модели на 90 градусов по оси Z
class RotateModelZOperator(bpy.types.Operator):
    bl_idname = "object.rotate_model_z"
    bl_label = "Rotate Z"
    
    def execute(self, context):
        # Получаем активный объект (выбранную модель)
        obj = context.active_object
        if obj:
            # Вращаем модель на 90 градусов по оси Z
            bpy.ops.transform.rotate(value=1.5708, orient_axis='Z', orient_type='GLOBAL', orient_matrix=((1, 0, 0), (0, 1, 0), (0, 0, 1)), orient_matrix_type='GLOBAL', constraint_axis=(False, False, True), mirror=False, use_proportional_edit=False, proportional_edit_falloff='SMOOTH', proportional_size=1, use_proportional_connected=False, use_proportional_projected=False, snap=False, snap_elements={'INCREMENT'}, use_snap_project=False, snap_target='CLOSEST', use_snap_self=True, use_snap_edit=True, use_snap_nonedit=True, use_snap_selectable=False, alt_navigation=True)
  # 90 градусов в радианах
        return {'FINISHED'}

# Определение оператора для вращения модели на 90 градусов по оси Y
class RotateModelYOperator(bpy.types.Operator):
    bl_idname = "object.rotate_model_y"
    bl_label = "Rotate Y"
    
    def execute(self, context):
        # Получаем активный объект (выбранную модель)
        obj = context.active_object
        if obj:
            # Вращаем модель на 90 градусов по оси Y
            bpy.ops.transform.rotate(value=1.5708, orient_axis='Y', orient_type='GLOBAL', orient_matrix=((1, 0, 0), (0, 1, 0), (0, 0, 1)), orient_matrix_type='GLOBAL', constraint_axis=(False, True, False), mirror=False, use_proportional_edit=False, proportional_edit_falloff='SMOOTH', proportional_size=1, use_proportional_connected=False, use_proportional_projected=False, snap=False, snap_elements={'INCREMENT'}, use_snap_project=False, snap_target='CLOSEST', use_snap_self=True, use_snap_edit=True, use_snap_nonedit=True, use_snap_selectable=False, alt_navigation=True)
  # 90 градусов в радианах
        return {'FINISHED'}




# Определение панели для отображения кнопок
class ModelImportPanel(bpy.types.Panel):
    bl_label = "Model Import Panel"
    bl_idname = "OBJECT_PT_model_import_panel"
    bl_space_type = 'VIEW_3D'
    bl_region_type = 'UI'
    bl_category = "Custom Addon" # Название вашей вкладки

    def draw(self, context):
        layout = self.layout
        # Добавляем кнопку для загрузки следующего файла
        layout.operator("object.load_next_file", text="Load Next File")
        # Добавляем кнопку для перехода на уровень выше
        layout.operator("object.go_up_level", text="Go Up Level")

# Определение панели для отображения кнопок вращения модели
class RotateModelPanel(bpy.types.Panel):
    bl_label = "Rotate Model Panel"
    bl_idname = "OBJECT_PT_rotate_model_panel"
    bl_space_type = 'VIEW_3D'
    bl_region_type = 'UI'
    bl_category = "Custom Addon" # Название вашей вкладки

    def draw(self, context):
        layout = self.layout
        # Добавляем кнопку для вызова оператора вращения по оси X
        layout.operator("object.rotate_model_x", text="Rotate X")
        # Добавляем кнопку для вызова оператора вращения по оси Y
        layout.operator("object.rotate_model_y", text="Rotate Y")
        # Добавляем кнопку для вызова оператора вращения по оси Z
        layout.operator("object.rotate_model_z", text="Rotate Z")
        # Добавляем кнопку для вызова оператора объединения модели
        layout.operator("object.join_model", text="Join")
    

# Регистрация классов
def register():
    bpy.utils.register_class(LoadNextFileOperator)
    bpy.utils.register_class(GoUpLevelOperator)
    bpy.utils.register_class(RotateModelXOperator)
    bpy.utils.register_class(RotateModelYOperator)
    bpy.utils.register_class(RotateModelZOperator)
    bpy.utils.register_class(ModelImportPanel)
    bpy.utils.register_class(RotateModelPanel)
    bpy.utils.register_class(ModelJoinOperator)
    
def unregister():
    bpy.utils.unregister_class(LoadNextFileOperator)
    bpy.utils.unregister_class(GoUpLevelOperator)
    bpy.utils.unregister_class(RotateModelXOperator)
    bpy.utils.unregister_class(RotateModelYOperator)
    bpy.utils.unregister_class(RotateModelZOperator)
    bpy.utils.unregister_class(ModelImportPanel)
    bpy.utils.unregister_class(RotateModelPanel)
    bpy.utils.unregister_class(ModelJoinOperator)
    
    
# Запуск аддона
if __name__ == "__main__":
    register()