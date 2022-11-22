from django.db import migrations, models

class Migration(migrations.Migration):

    dependencies = [
        ('app', '0001_initial')
    ]

    operations = [
        migrations.RunSQL(
            sql="INSERT INTO app_produtos(nome, preco, quantidade, imagem) VALUES('Whey Protein Concentrado', 99.98, 122, 'https://a-static.mlcdn.com.br/800x560/whey-protein-concentrado-900g-dux-nutrition/sefsportsuplementos/14e5dea8dea711ec84a04201ac185078/36c1185bdaa477825c0b3b6d640c4045.jpeg');INSERT INTO app_produtos(nome, preco, quantidade, imagem) VALUES('Whey Protein Isolado', 135.98, 67, 'https://duxnutrition.vtexassets.com/arquivos/ids/161320-1200-auto?v=637695835515230000&width=1200&height=auto&aspect=true');INSERT INTO app_produtos(nome, preco, quantidade, imagem) VALUES('Pre-Treino', 103.50, 124, 'https://a-static.mlcdn.com.br/800x560/suplemento-horus-pre-treino-resistencia-e-desempenho-limao-yuzu-300g-max-titanium/cr10suplementos/bddb7898aff911eb8fc44201ac18500e/a8266ccb73ed76af1866e2f9c1942f34.jpeg');INSERT INTO app_produtos(nome, preco, quantidade, imagem) VALUES('Strap', 45.60, 80, 'https://m.media-amazon.com/images/I/71HrV2OzqvS._AC_SX679_.jpg');INSERT INTO app_produtos(nome, preco, quantidade, imagem) VALUES('Creatina 250g', 100.98, 25, 'https://www.gsuplementos.com.br/upload/growth-layout-personalizado/produto/72/creatina-monohidratada-growth.png');INSERT INTO app_produtos(nome, preco, quantidade, imagem) VALUES('Creatina 100g', 80.50, 76, 'https://www.gsuplementos.com.br/upload/growth-layout-personalizado/produto/69/creatina-creapure-100g-growth-supplements.png');INSERT INTO app_produtos(nome, preco, quantidade, imagem) VALUES('Cafeina 60Caps', 62.70, 90, 'https://www.gsuplementos.com.br/upload/produto/layout/39/cafeina-420mg-60caps-growth-supplements.webp');INSERT INTO app_produtos(nome, preco, quantidade, imagem) VALUES('Cafeina 120Caps', 120.67, 40, 'https://www.gsuplementos.com.br/upload/growth-layout-personalizado/produto/36/cafeina-210mg-120caps-growth-supplements.png');INSERT INTO app_produtos(nome, preco, quantidade, imagem) VALUES('Garrafa', 20.00, 100, 'https://www.gsuplementos.com.br/upload/produto/imagem/b_squeeze-growth-800ml-growth-supplements-3.png');INSERT INTO app_produtos(nome, preco, quantidade, imagem) VALUES('Galão 2L', 40.00, 45, 'https://www.gsuplementos.com.br/upload/growth-layout-personalizado/produto/1363/galao-2litros-growth-supplements-transparente-v3.png');INSERT INTO app_produtos(nome, preco, quantidade, imagem) VALUES('Coqueteleira', 10.00, 150, 'https://www.gsuplementos.com.br/upload/produto/imagem/b_coqueteleira-simples-branca-growth-supplements.jpeg');INSERT INTO app_produtos(nome, preco, quantidade, imagem) VALUES('Coqueteleira 3Compartimentos', 20.00, 100, 'https://www.gsuplementos.com.br/upload/produto/imagem/b_coqueteleira-3-compartimentos-com-mixball-growth-supplements.png');"
        )
    ]