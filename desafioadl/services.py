# agregar from .models e importar las clases
from .models import Tarea, SubTarea

# agregar los métodos de creación de instancias
# 6. Dentro del archivo services.py crear 6 funciones: 
# a. recupera_tareas_y_sub_tareas 
# b. crear_nueva_tarea 
# c. crear_sub_tarea 
# d. elimina_tarea 
# e. elimina_sub_tarea 
# f. imprimir_en_pantalla  


def recupera_tareas_y_sub_tareas():
    tareas = Tarea.objects.all()
    subtareas = SubTarea.objects.all()
    return tareas, subtareas

def crear_nueva_tarea(descripcion):
    tarea = Tarea(descripcion=descripcion)
    tarea.save()
    return tarea

def crear_sub_tarea(descripcion, tarea_id):
    subtarea = SubTarea(descripcion=descripcion, tarea_id=tarea_id)
    subtarea.save()
    return subtarea

def elimina_tarea(tarea_id):
    tarea = Tarea.objects.get(id=tarea_id)
    tarea.delete()
    return tarea

def elimina_sub_tarea(subtarea_id):
    subtarea = SubTarea.objects.get(id=subtarea_id)
    subtarea.delete()
    return subtarea

def imprimir_en_pantalla(tareas_subtareas):
    tareas, subtareas = tareas_subtareas
    for tarea in tareas:
        print(f'[{tarea.id}] {tarea.descripcion}')
        for sub_tarea in subtareas.filter(tarea=tarea):
            print(f'.... [{sub_tarea.id}] {sub_tarea.descripcion}')