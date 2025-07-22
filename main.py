import tkinter as tk
from tkinter import ttk, messagebox, simpledialog
import json
import os
from datetime import datetime

class CongregacionManager:
    def __init__(self):
        self.root = tk.Tk()
        self.root.title("Sistema de Congregaciones")
        self.root.geometry("800x600")
        self.root.configure(bg='#f8f9fa')
        
        # Archivo para guardar datos
        self.data_file = "congregaciones.json"
        self.congregaciones = self.cargar_datos()
        
        self.crear_ventana_principal()
        
    def cargar_datos(self):
        """Carga los datos desde el archivo JSON"""
        if os.path.exists(self.data_file):
            try:
                with open(self.data_file, 'r', encoding='utf-8') as f:
                    return json.load(f)
            except:
                return []
        return []
    
    def guardar_datos(self):
        """Guarda los datos en el archivo JSON"""
        try:
            with open(self.data_file, 'w', encoding='utf-8') as f:
                json.dump(self.congregaciones, f, ensure_ascii=False, indent=2)
            return True
        except:
            return False
    
    def crear_ventana_principal(self):
        """Crea la ventana principal de la aplicación"""
        # Limpiar ventana
        for widget in self.root.winfo_children():
            widget.destroy()
            
        # Frame principal
        main_frame = tk.Frame(self.root, bg='#f8f9fa')
        main_frame.pack(expand=True, fill='both', padx=20, pady=20)
        
        # Título principal
        title_label = tk.Label(
            main_frame, 
            text="Sistema de Congregaciones",
            font=('Arial', 24, 'bold'),
            bg='#f8f9fa',
            fg='#212529'
        )
        title_label.pack(pady=(50, 20))
        
        # Subtítulo
        subtitle_label = tk.Label(
            main_frame,
            text="Gestiona las congregaciones de tu organización",
            font=('Arial', 12),
            bg='#f8f9fa',
            fg='#6c757d'
        )
        subtitle_label.pack(pady=(0, 50))
        
        # Botón principal
        btn_abrir = tk.Button(
            main_frame,
            text="Abrir Gestor de Congregaciones",
            font=('Arial', 12, 'bold'),
            bg='#007bff',
            fg='white',
            padx=30,
            pady=15,
            cursor='hand2',
            command=self.mostrar_modal_cargar
        )
        btn_abrir.pack(pady=20)
        
        # Mostrar estadísticas
        stats_frame = tk.Frame(main_frame, bg='#f8f9fa')
        stats_frame.pack(pady=30)
        
        stats_label = tk.Label(
            stats_frame,
            text=f"Congregaciones registradas: {len(self.congregaciones)}",
            font=('Arial', 10),
            bg='#f8f9fa',
            fg='#6c757d'
        )
        stats_label.pack()
        
        # Botón para ver lista (si hay congregaciones)
        if self.congregaciones:
            btn_ver_lista = tk.Button(
                main_frame,
                text="Ver Lista de Congregaciones",
                font=('Arial', 10),
                bg='#28a745',
                fg='white',
                padx=20,
                pady=10,
                cursor='hand2',
                command=self.mostrar_lista_congregaciones
            )
            btn_ver_lista.pack(pady=10)
    
    def mostrar_modal_cargar(self):
        """Muestra el modal para cargar nueva congregación"""
        modal = tk.Toplevel(self.root)
        modal.title("Cargar Nueva Congregación")
        modal.geometry("400x300")
        modal.configure(bg='white')
        modal.resizable(False, False)
        
        # Centrar modal
        modal.transient(self.root)
        modal.grab_set()
        
        # Título del modal
        title_frame = tk.Frame(modal, bg='white')
        title_frame.pack(fill='x', padx=20, pady=20)
        
        title_label = tk.Label(
            title_frame,
            text="Cargar Nueva Congregación",
            font=('Arial', 16, 'bold'),
            bg='white',
            fg='#212529'
        )
        title_label.pack()
        
        # Contenido del modal
        content_frame = tk.Frame(modal, bg='white')
        content_frame.pack(expand=True, fill='both', padx=20, pady=20)
        
        description_label = tk.Label(
            content_frame,
            text="Haz clic en el botón para acceder al\nformulario de registro de congregación",
            font=('Arial', 11),
            bg='white',
            fg='#6c757d',
            justify='center'
        )
        description_label.pack(pady=30)
        
        # Botón para ir al formulario
        btn_formulario = tk.Button(
            content_frame,
            text="Ir al Formulario",
            font=('Arial', 12, 'bold'),
            bg='#007bff',
            fg='white',
            padx=40,
            pady=12,
            cursor='hand2',
            command=lambda: [modal.destroy(), self.mostrar_formulario()]
        )
        btn_formulario.pack(pady=20)
        
        # Botón cerrar
        btn_cerrar = tk.Button(
            content_frame,
            text="Cerrar",
            font=('Arial', 10),
            bg='#6c757d',
            fg='white',
            padx=20,
            pady=8,
            cursor='hand2',
            command=modal.destroy
        )
        btn_cerrar.pack(pady=10)
    
    def mostrar_formulario(self):
        """Muestra el formulario para cargar congregación"""
        form_window = tk.Toplevel(self.root)
        form_window.title("Formulario de Congregación")
        form_window.geometry("600x500")
        form_window.configure(bg='#f8f9fa')
        
        # Header con botón de regreso
        header_frame = tk.Frame(form_window, bg='#f8f9fa')
        header_frame.pack(fill='x', padx=20, pady=20)
        
        btn_volver = tk.Button(
            header_frame,
            text="← Volver",
            font=('Arial', 10),
            bg='#6c757d',
            fg='white',
            padx=15,
            pady=5,
            cursor='hand2',
            command=form_window.destroy
        )
        btn_volver.pack(side='left')
        
        title_label = tk.Label(
            header_frame,
            text="Cargar Nueva Congregación",
            font=('Arial', 18, 'bold'),
            bg='#f8f9fa',
            fg='#212529'
        )
        title_label.pack(side='left', padx=(20, 0))
        
        # Frame principal del formulario
        form_frame = tk.LabelFrame(
            form_window,
            text="Información de la Congregación",
            font=('Arial', 12, 'bold'),
            bg='white',
            fg='#212529',
            padx=20,
            pady=20
        )
        form_frame.pack(fill='both', expand=True, padx=20, pady=20)
        
        # Campo nombre
        tk.Label(
            form_frame,
            text="Nombre de la Congregación *",
            font=('Arial', 11, 'bold'),
            bg='white',
            fg='#212529'
        ).pack(anchor='w', pady=(10, 5))
        
        entry_nombre = tk.Entry(
            form_frame,
            font=('Arial', 11),
            width=50,
            relief='solid',
            borderwidth=1
        )
        entry_nombre.pack(fill='x', pady=(0, 5))
        
        tk.Label(
            form_frame,
            text="Ingresa el nombre completo de la congregación",
            font=('Arial', 9),
            bg='white',
            fg='#6c757d'
        ).pack(anchor='w', pady=(0, 15))
        
        # Campo ID
        tk.Label(
            form_frame,
            text="ID de la Congregación *",
            font=('Arial', 11, 'bold'),
            bg='white',
            fg='#212529'
        ).pack(anchor='w', pady=(10, 5))
        
        entry_id = tk.Entry(
            form_frame,
            font=('Arial', 11),
            width=50,
            relief='solid',
            borderwidth=1
        )
        entry_id.pack(fill='x', pady=(0, 5))
        
        tk.Label(
            form_frame,
            text="Código único identificador para la congregación",
            font=('Arial', 9),
            bg='white',
            fg='#6c757d'
        ).pack(anchor='w', pady=(0, 20))
        
        # Botones de acción
        buttons_frame = tk.Frame(form_frame, bg='white')
        buttons_frame.pack(fill='x', pady=20)
        
        def guardar_congregacion():
            nombre = entry_nombre.get().strip()
            id_cong = entry_id.get().strip()
            
            if not nombre or not id_cong:
                messagebox.showerror("Error", "Por favor completa todos los campos")
                return
            
            # Verificar ID único
            for cong in self.congregaciones:
                if cong['id'] == id_cong:
                    messagebox.showerror("Error", "El ID de congregación ya existe")
                    return
            
            # Guardar congregación
            nueva_congregacion = {
                'id': id_cong,
                'nombre': nombre,
                'fecha_registro': datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            }
            
            self.congregaciones.append(nueva_congregacion)
            
            if self.guardar_datos():
                messagebox.showinfo("¡Éxito!", f'Congregación "{nombre}" guardada correctamente')
                entry_nombre.delete(0, tk.END)
                entry_id.delete(0, tk.END)
                self.crear_ventana_principal()  # Actualizar ventana principal
            else:
                messagebox.showerror("Error", "No se pudo guardar la congregación")
        
        def limpiar_campos():
            entry_nombre.delete(0, tk.END)
            entry_id.delete(0, tk.END)
        
        btn_guardar = tk.Button(
            buttons_frame,
            text="💾 Guardar Congregación",
            font=('Arial', 11, 'bold'),
            bg='#28a745',
            fg='white',
            padx=20,
            pady=10,
            cursor='hand2',
            command=guardar_congregacion
        )
        btn_guardar.pack(side='left', padx=(0, 10))
        
        btn_limpiar = tk.Button(
            buttons_frame,
            text="🗑️ Limpiar Campos",
            font=('Arial', 11),
            bg='#6c757d',
            fg='white',
            padx=20,
            pady=10,
            cursor='hand2',
            command=limpiar_campos
        )
        btn_limpiar.pack(side='left')
        
        # Información adicional
        info_frame = tk.LabelFrame(
            form_window,
            text="Información importante",
            font=('Arial', 10, 'bold'),
            bg='#e3f2fd',
            fg='#1565c0',
            padx=15,
            pady=10
        )
        info_frame.pack(fill='x', padx=20, pady=(0, 20))
        
        info_text = tk.Label(
            info_frame,
            text="• Asegúrate de que el ID de la congregación sea único y fácil de recordar\n• Una vez guardado, podrás gestionar los miembros y actividades de esta congregación\n• Los datos se guardan automáticamente en 'congregaciones.json'",
            font=('Arial', 9),
            bg='#e3f2fd',
            fg='#1565c0',
            justify='left'
        )
        info_text.pack(anchor='w')
    
    def mostrar_lista_congregaciones(self):
        """Muestra la lista de congregaciones registradas"""
        list_window = tk.Toplevel(self.root)
        list_window.title("Lista de Congregaciones")
        list_window.geometry("700x500")
        list_window.configure(bg='#f8f9fa')
        
        # Header
        header_frame = tk.Frame(list_window, bg='#f8f9fa')
        header_frame.pack(fill='x', padx=20, pady=20)
        
        btn_volver = tk.Button(
            header_frame,
            text="← Volver",
            font=('Arial', 10),
            bg='#6c757d',
            fg='white',
            padx=15,
            pady=5,
            cursor='hand2',
            command=list_window.destroy
        )
        btn_volver.pack(side='left')
        
        title_label = tk.Label(
            header_frame,
            text="Lista de Congregaciones",
            font=('Arial', 18, 'bold'),
            bg='#f8f9fa',
            fg='#212529'
        )
        title_label.pack(side='left', padx=(20, 0))
        
        # Tabla de congregaciones
        table_frame = tk.Frame(list_window, bg='white')
        table_frame.pack(fill='both', expand=True, padx=20, pady=20)
        
        # Crear Treeview
        columns = ('ID', 'Nombre', 'Fecha Registro')
        tree = ttk.Treeview(table_frame, columns=columns, show='headings', height=15)
        
        # Configurar columnas
        tree.heading('ID', text='ID')
        tree.heading('Nombre', text='Nombre de Congregación')
        tree.heading('Fecha Registro', text='Fecha de Registro')
        
        tree.column('ID', width=100)
        tree.column('Nombre', width=300)
        tree.column('Fecha Registro', width=150)
        
        # Agregar datos
        for cong in self.congregaciones:
            tree.insert('', 'end', values=(
                cong['id'],
                cong['nombre'],
                cong.get('fecha_registro', 'N/A')
            ))
        
        # Scrollbar
        scrollbar = ttk.Scrollbar(table_frame, orient='vertical', command=tree.yview)
        tree.configure(yscrollcommand=scrollbar.set)
        
        tree.pack(side='left', fill='both', expand=True)
        scrollbar.pack(side='right', fill='y')
    
    def ejecutar(self):
        """Ejecuta la aplicación"""
        self.root.mainloop()

# Ejecutar la aplicación
if __name__ == "__main__":
    app = CongregacionManager()
    app.ejecutar()