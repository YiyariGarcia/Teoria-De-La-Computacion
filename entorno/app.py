import flet as ft
from lenguajes import obtener_prefijos, obtener_sufijos, obtener_subcadenas, calcular_cerradura

def main(page: ft.Page):
    page.title = "Teoría de Lenguajes Formales"
    page.theme_mode = ft.ThemeMode.LIGHT
    page.padding = 20

    def guardar_archivo(e: ft.FilePickerResultEvent, contenido: str):
        if e.path:
            with open(e.path, "w", encoding="utf-8") as f:
                f.write(contenido)
            page.snack_bar = ft.SnackBar(ft.Text("Archivo guardado correctamente"))
            page.snack_bar.open = True
            page.update()

    picker_dialog = ft.FilePicker(on_result=lambda e: guardar_archivo(e, page.session.get("texto_a_guardar")))
    page.overlay.append(picker_dialog)

    # --- Operación 1 ---
    txt_cadena = ft.TextField(label="Ingrese una cadena", width=300)
    resultado_op1 = ft.TextField(multiline=True, read_only=True, min_lines=5, max_lines=15)

    def procesar_cadena(e):
        cadena = txt_cadena.value
        prefijos = obtener_prefijos(cadena)
        sufijos = obtener_sufijos(cadena)
        subcadenas = obtener_subcadenas(cadena)
        
        texto = f"--- PREFIJOS ({len(prefijos)}) ---\n{prefijos}\n\n"
        texto += f"--- SUFIJOS ({len(sufijos)}) ---\n{sufijos}\n\n"
        texto += f"--- SUBCADENAS ({len(subcadenas)}) ---\n{subcadenas}"
        
        resultado_op1.value = texto
        page.session.set("texto_a_guardar", texto)
        btn_guardar_op1.disabled = False
        page.update()

    btn_procesar_op1 = ft.ElevatedButton("Procesar Cadena", on_click=procesar_cadena)
    btn_guardar_op1 = ft.FilledButton("Guardar Resultados", icon=ft.icons.SAVE, disabled=True, on_click=lambda _: picker_dialog.save_file(file_name="subcadenas.txt"))

    # --- Operación 2 ---
    txt_alfabeto = ft.TextField(label="Alfabeto (ej. ab)", width=150)
    txt_n = ft.TextField(label="Longitud (n)", width=100, keyboard_type=ft.KeyboardType.NUMBER)
    resultado_op2 = ft.TextField(multiline=True, read_only=True, min_lines=5, max_lines=15)

    def procesar_cerradura(e, es_positiva):
        try:
            n = int(txt_n.value)
            resultado = calcular_cerradura(txt_alfabeto.value, n, es_positiva)
            tipo = "Σ+" if es_positiva else "Σ*"
            
            # Reemplazar cadena vacía por epsilon para visualización
            display_res = ["ε" if x == "" else x for x in resultado]
            
            texto = f"--- CERRADURA {tipo} (n={n}) ---\nTotal generadas: {len(resultado)}\n\n{display_res}"
            resultado_op2.value = texto
            page.session.set("texto_a_guardar", texto)
            btn_guardar_op2.disabled = False
        except ValueError as ex:
            resultado_op2.value = f"ERROR: {str(ex)}"
            btn_guardar_op2.disabled = True
        page.update()

    btn_kleene = ft.ElevatedButton("Calcular Σ*", on_click=lambda e: procesar_cerradura(e, es_positiva=False))
    btn_positiva = ft.ElevatedButton("Calcular Σ+", on_click=lambda e: procesar_cerradura(e, es_positiva=True))
    btn_guardar_op2 = ft.FilledButton("Guardar Resultados", icon=ft.icons.SAVE, disabled=True, on_click=lambda _: picker_dialog.save_file(file_name="cerradura.txt"))

    # Estructura visual con pestañas
    t = ft.Tabs(
        selected_index=0,
        tabs=[
            ft.Tab(
                text="Operación 1: Cadenas",
                content=ft.Column([ft.Row([txt_cadena, btn_procesar_op1]), resultado_op1, btn_guardar_op1])
            ),
            ft.Tab(
                text="Operación 2: Cerraduras",
                content=ft.Column([ft.Row([txt_alfabeto, txt_n, btn_kleene, btn_positiva]), resultado_op2, btn_guardar_op2])
            ),
        ],
        expand=1
    )
    page.add(t)

# Para servir en navegador (contenedor py312):
ft.app(target=main, view=ft.AppView.WEB_BROWSER, port=8000, host="0.0.0.0")