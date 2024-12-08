import random
import tkinter as tk
import ttkbootstrap as ttk

from data import SystemFeature
from data import SYSTEM_FEATURES

class SystemCreationFrame(ttk.Labelframe):
    SelectedSystemFeature: SystemFeature
    SelectedSystemFeatureDescription: tk.StringVar
    
    def __init__(self, master = None):
        super().__init__(master, text='STEP 1: SYSTEM CREATION')
        
        self.init_variables()
        self.configure_layout()
        self.create_widgets()
     
     
    def init_variables(self):
        self.SelectedSystemFeatureDescription = tk.StringVar()
     
    def configure_layout(self):
        self.columnconfigure(0, weight=10)
        self.columnconfigure(1, weight=1)
        self.columnconfigure(2, weight=1)
        
        self.rowconfigure(0, weight=1)
        self.rowconfigure(1, weight=1)
        self.rowconfigure(2, weight=1)
        self.rowconfigure(3, weight=1)
        
    def create_widgets(self):
        ttk.Label(self, text='System Features').grid(column=0, columnspan=2, row=0, padx=5, pady=5, sticky='w')
        
        self.FeatureComboBox = ttk.Combobox(self, values=[str(f) for f in SYSTEM_FEATURES], state='readonly')
        self.FeatureComboBox.grid(column=0, row=1, padx=5, pady=5, sticky='we')
        self.FeatureComboBox.bind("<<ComboboxSelected>>", self.select_feature)
        
        self.FeatureButton = ttk.Button(self, text='R', command=self.random_feature)
        self.FeatureButton.grid(column=1, row=1)
        
        label = ttk.Label(self, textvariable=self.SelectedSystemFeatureDescription)
        label.grid(column=0, columnspan=2, row=2, padx=5, pady=5, sticky='we')
        label.bind('<Configure>', lambda e: label.config(wraplength=label.winfo_width()))
        
    #region System Features
    
    def random_feature(self):
        # self.update_feature_display()
        feature = random.choice(SYSTEM_FEATURES)
        self.FeatureComboBox.set(str(feature))
    
    def select_feature(self, event):
        selected_name = self.FeatureComboBox.get()
        feature = next((f for f in SYSTEM_FEATURES if str(f) == selected_name), None)
        if feature:
            self.SelectedSystemFeature = feature
            self.update_feature_display()
    
    def update_feature_display(self):
        self.SelectedSystemFeatureDescription.set(self.SelectedSystemFeature.Description)
        
    
    #endregion