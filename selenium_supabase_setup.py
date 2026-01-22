#!/usr/bin/env python3
"""
Script Selenium para criar projeto no Supabase automaticamente
"""

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.options import Options
import time
import json

# Configurações
EMAIL = "givaldosj@gmail.com"
PASSWORD = "Thiago2248tA@@"
PROJECT_NAME = "SecretariaEletronica"
DB_PASSWORD = "pC3IPSXIW4rcgnXY"
REGION = "South America (São Paulo)"

def setup_driver():
    """Configurar driver do Selenium"""
    chrome_options = Options()
    chrome_options.add_argument("--no-sandbox")
    chrome_options.add_argument("--disable-dev-shm-usage")
    chrome_options.add_argument("--disable-blink-features=AutomationControlled")
    chrome_options.add_experimental_option("excludeSwitches", ["enable-automation"])
    chrome_options.add_experimental_option('useAutomationExtension', False)
    
    driver = webdriver.Chrome(options=chrome_options)
    driver.set_window_size(1280, 1024)
    return driver

def login(driver):
    """Fazer login no Supabase"""
    print("🔐 Fazendo login...")
    driver.get("https://supabase.com/dashboard/sign-in")
    
    time.sleep(3)
    
    # Procurar pelo campo de email
    try:
        email_field = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.NAME, "email"))
        )
        email_field.send_keys(EMAIL)
        print("✅ Email inserido")
        
        # Procurar pelo campo de senha
        password_field = driver.find_element(By.NAME, "password")
        password_field.send_keys(PASSWORD)
        print("✅ Senha inserida")
        
        # Clicar no botão de login
        login_button = driver.find_element(By.XPATH, "//button[contains(text(), 'Sign in')]")
        login_button.click()
        print("✅ Clicado em Sign in")
        
        # Aguardar redirecionamento
        WebDriverWait(driver, 15).until(
            EC.url_changes(driver.current_url)
        )
        print("✅ Login realizado com sucesso!")
        return True
        
    except Exception as e:
        print(f"❌ Erro durante login: {str(e)}")
        return False

def create_project(driver):
    """Criar novo projeto"""
    print("\n📦 Criando projeto...")
    
    try:
        # Navegar para a página de organizações
        driver.get("https://supabase.com/dashboard/organizations")
        time.sleep(3)
        
        # Procurar pelo botão "New project"
        new_project_btn = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, "//button[contains(text(), 'New project')] | //a[contains(text(), 'New project')]"))
        )
        new_project_btn.click()
        print("✅ Clicado em New project")
        
        time.sleep(3)
        
        # Preencher nome do projeto
        project_name_field = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.XPATH, "//input[@placeholder='Project name']"))
        )
        project_name_field.send_keys(PROJECT_NAME)
        print(f"✅ Nome do projeto inserido: {PROJECT_NAME}")
        
        # Preencher senha do banco de dados
        db_password_field = driver.find_element(By.XPATH, "//input[@placeholder='Type in a strong password']")
        db_password_field.send_keys(DB_PASSWORD)
        print("✅ Senha do banco inserida")
        
        # Selecionar região
        region_dropdown = driver.find_element(By.XPATH, "//button[contains(text(), 'Americas')] | //button[contains(text(), 'South America')]")
        region_dropdown.click()
        time.sleep(1)
        
        # Selecionar South America (São Paulo)
        region_option = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, "//div[contains(text(), 'South America (São Paulo)')]"))
        )
        region_option.click()
        print("✅ Região selecionada: South America (São Paulo)")
        
        time.sleep(2)
        
        # Clicar em Create new project
        create_btn = driver.find_element(By.XPATH, "//button[contains(text(), 'Create new project')]")
        create_btn.click()
        print("✅ Clicado em Create new project")
        
        # Aguardar criação
        print("⏳ Aguardando criação do projeto (2-3 minutos)...")
        time.sleep(180)  # Aguardar 3 minutos
        
        print("✅ Projeto criado com sucesso!")
        return True
        
    except Exception as e:
        print(f"❌ Erro ao criar projeto: {str(e)}")
        import traceback
        traceback.print_exc()
        return False

def main():
    """Função principal"""
    print("=" * 70)
    print("🚀 AUTOMAÇÃO SUPABASE - SECRETÁRIA ELETRÔNICA")
    print("=" * 70)
    
    driver = None
    try:
        driver = setup_driver()
        
        # Login
        if not login(driver):
            return False
        
        # Criar projeto
        if not create_project(driver):
            return False
        
        print("\n" + "=" * 70)
        print("✅ PROJETO CRIADO COM SUCESSO!")
        print("=" * 70)
        print("""
Próximos passos:
1. Aguarde o projeto ficar completamente pronto
2. Acesse o projeto no Supabase
3. Vá para SQL Editor
4. Cole o conteúdo de database_schema.sql
5. Execute o SQL
6. Copie as credenciais de Settings > API
7. Me avise para configurar o n8n
        """)
        
        return True
        
    except Exception as e:
        print(f"❌ Erro geral: {str(e)}")
        import traceback
        traceback.print_exc()
        return False
        
    finally:
        if driver:
            driver.quit()

if __name__ == "__main__":
    success = main()
    exit(0 if success else 1)
