import requests
from bs4 import BeautifulSoup

url = "https://lista.mercadolivre.com.br/veiculos/carros-caminhonetes/e-financiavel/"

response = requests.get(url)

if response.status_code == 200:
    soup = BeautifulSoup(response.content, "html.parser")

    product_containers = soup.find_all(
        "div", class_="ui-search-result__content-wrapper"
    )

    for container in product_containers:
        product_name_elem = container.find("h2", class_="ui-search-item__title")
        product_name = (
            product_name_elem.text.strip()
            if product_name_elem
            else "Nome do produto não disponível"
        )

        price_elem = container.find("div", class_="ui-search-item__group--price")
        if not price_elem:
            price_elem = container.find(
                "div",
                class_="ui-search-item__group ui-search-item__group--price-grid-container",
            )

        price_fraction_elem = container.find(
            "span", class_="andes-money-amount__fraction"
        )
        product_price = (
            price_fraction_elem.text.strip()
            if price_fraction_elem
            else "Preço não disponível"
        )

        print(f"Produto: {product_name}\nPreço: {product_price}\n")

else:
    print(f"Erro ao acessar a página: {response.status_code}")
