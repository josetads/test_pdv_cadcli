import os
from selenium import webdriver
from selenium.webdriver.firefox.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

# Caminho absoluto para o geckodriver
geckodriver_path = r"D:\CONCURSOS_PROCESSOS_SELETIVOS\FAEPI_IFAM2024ProfessorFormador\AulasFICAranoua_CTDI\Projetos_Selenium\testepdv\geckodriver.exe"

# Verifica se o geckodriver existe no caminho especificado
if not os.path.isfile(geckodriver_path):
    raise FileNotFoundError(f"Geckodriver não encontrado no caminho: {geckodriver_path}")

# Caminho para o executável do Firefox
firefox_binary_path = r"C:\Program Files\Mozilla Firefox\firefox.exe"  # Caminho padrão no Windows

# Verifica se o Firefox existe no caminho especificado
if not os.path.isfile(firefox_binary_path):
    raise FileNotFoundError(f"Firefox não encontrado no caminho: {firefox_binary_path}")

# Configuração do Firefox com caminho explícito para o executável
options = webdriver.FirefoxOptions()
options.binary_location = firefox_binary_path

# Configuração do serviço do geckodriver
service = Service(geckodriver_path)

# Inicializando o WebDriver
driver = webdriver.Firefox(service=service, options=options)

try:
    # Acesse a página de login
    driver.get("http://localhost/pdv/login")

    # Aguarde carregar a página
    time.sleep(2)

    # Localize os campos de e-mail e senha
    email_field = driver.find_element(By.ID, "inputEmail")
    password_field = driver.find_element(By.ID, "inputPassword")

    # Insira as credenciais
    email_field.send_keys("erico2223@gmail.com")
    password_field.send_keys("123")

    # Envie o formulário
    password_field.send_keys(Keys.RETURN)

    # Aguarde para verificar se o login foi bem-sucedido
    time.sleep(5)

    # Verifica se redirecionou para outra página ou se existe algum elemento de erro
    if "login" not in driver.current_url.lower():
        print("Login realizado com sucesso!")

        # Acesse a página de cadastro de cliente
        driver.get("http://localhost/pdv/cliente/cadastro")

        # Aguarde carregar a página
        time.sleep(2)

        # Preencher os campos de cadastro de cliente
        nome_field = driver.find_element(By.ID, "nome")
        cpf_field = driver.find_element(By.ID, "cpf")
        telefone_field = driver.find_element(By.ID, "telefone")
        ativo_checkbox = driver.find_element(By.ID, "ativo")

        # Preencher os dados do cliente (exemplo)
        nome_field.send_keys("João Silva")
        cpf_field.send_keys("123.456.789-00")
        telefone_field.send_keys("9876543210")
        if not ativo_checkbox.is_selected():
            ativo_checkbox.click()  # Marca o cliente como ativo

        # Enviar o formulário
        submit_button = driver.find_element(By.ID, "submitCadastro")
        submit_button.click()

        # Aguarde para verificar o cadastro
        time.sleep(3)

        # Verifique se o cadastro foi bem-sucedido
        if "cliente" in driver.current_url.lower():
            print("Cadastro de cliente realizado com sucesso!")
        else:
            print("Falha ao cadastrar cliente.")
    else:
        print("Falha no login. Verifique as credenciais ou o sistema.")
finally:
    # Fechar o navegador
    driver.quit()
