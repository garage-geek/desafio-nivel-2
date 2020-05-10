"""Require running database server"""
import json


async def test_index(cli, tables_and_data):
    response = await cli.get('/')
    assert response.status == 200


async def test_index_text(cli, tables_and_data):
    response = await cli.get('/')
    assert 'Detalhe Cidades' in await response.text()


async def test_city(cli, tables_and_data):
    response = await cli.get('/city')
    assert response.status == 200


async def test_city_text(cli, tables_and_data):
    response = await cli.get('/city')
    assert 'Cadastro de Cidade' in await response.text()
    assert 'Escolha um Estado' in await response.text()


async def test_state(cli, tables_and_data):
    response = await cli.get('/state')
    assert response.status == 200


async def test_state_text(cli, tables_and_data):
    response = await cli.get('/state')
    assert 'Cadastro de Estado' in await response.text()


async def test_minas_city_results(cli, tables_and_data):
    response = await cli.get('/state_city/1')
    assert response.status == 200
    assert 'Belo Horizonte' in await response.text()
    assert 'Sabará' in await response.text()
    assert 'Minas Gerais' in await response.text()


async def test_rio_grande_do_sul_city_results(cli, tables_and_data):
    response = await cli.get('/state_city/2')
    assert response.status == 200
    assert 'Caxias do Sul' in await response.text()
    assert 'Rio Grande do Sul' in await response.text()


async def test_state_results(cli, tables_and_data):
    response = await cli.get('/')
    assert response.status == 200
    assert 'Minas Gerais' in await response.text()
    assert 'Rio Grande do Sul' in await response.text()


async def test_no_exist_url(cli, tables_and_data):
    response = await cli.get('/no_exist_url')
    assert '404 Página não encontrada. O endereço que você solicitou não existe.' in await response.text()


async def test_add_state(cli, tables_and_data):
    response = await cli.post(
        f'/api/state',
        data=json.dumps({'state_name': 'Mato Grosso'})
    )
    assert response.status == 200
    response = await cli.get('/')
    assert response.status == 200
    assert 'Mato Grosso' in await response.text()


async def test_add_city(cli, tables_and_data):
    response = await cli.post(
        f'/api/city',
        data=json.dumps({'city_name': 'Betim', 'state_id': '1'})
    )
    assert response.status == 200
    response = await cli.get('state_city/1')
    assert response.status == 200
    assert 'Betim' in await response.text()
    assert 'Belo Horizonte' in await response.text()
    assert 'Sabará' in await response.text()
    assert 'Minas Gerais' in await response.text()
