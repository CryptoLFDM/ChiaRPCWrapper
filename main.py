import requests
import urllib3
import click
from flask import Flask

api = Flask(__name__)
urllib3.disable_warnings()

headers = {'Content-Type': 'application/json'}
chia_root_path = None


@api.route('/get_blockchain_state', methods=['GET'])
def get_blockchain_state():
    url = 'https://localhost:8555/get_blockchain_state'
    cert = '{}/config/ssl/full_node/private_full_node.crt'.format(chia_root_path)
    key = '{}/config/ssl/full_node/private_full_node.key'.format(chia_root_path)
    return make_request(url, cert, key)


@api.route('/get_network_space', methods=['GET'])
def get_network_space():
    url = 'https://localhost:8555/get_network_space'
    cert = '{}/config/ssl/full_node/private_full_node.crt'.format(chia_root_path)
    key = '{}/config/ssl/full_node/private_full_node.key'.format(chia_root_path)
    return make_request(url, cert, key)


@api.route('/healthz', methods=['GET'])
def healthz():
    url = 'https://localhost:8555/healthz'
    cert = '{}/config/ssl/full_node/private_full_node.crt'.format(chia_root_path)
    key = '{}/config/ssl/full_node/private_full_node.key'.format(chia_root_path)
    return make_request(url, cert, key)


@api.route('/get_pool_state', methods=['GET'])
def get_pool_state():
    url = 'https://localhost:8559/get_pool_state'
    cert = '{}/config/ssl/farmer/private_farmer.crt'.format(chia_root_path)
    key = '{}/config/ssl/farmer/private_farmer.key'.format(chia_root_path)
    return make_request(url, cert, key)


@api.route('/get_harvesters', methods=['GET'])
def get_harvesters():
    url = 'https://localhost:8559/get_harvesters'
    cert = '{}/config/ssl/farmer/private_farmer.crt'.format(chia_root_path)
    key = '{}/config/ssl/farmer/private_farmer.key'.format(chia_root_path)
    return make_request(url, cert, key)


@api.route('/get_harvesters_summary', methods=['GET'])
def get_harvesters_summary():
    url = 'https://localhost:8559/get_harvesters_summary'
    cert = '{}/config/ssl/farmer/private_farmer.crt'.format(chia_root_path)
    key = '{}/config/ssl/farmer/private_farmer.key'.format(chia_root_path)
    return make_request(url, cert, key)


@api.route('/get_harvester_plots_valid', methods=['GET'])
def get_harvester_plots_valid():
    url = 'https://localhost:8559/get_harvester_plots_valid'
    cert = '{}/config/ssl/farmer/private_farmer.crt'.format(chia_root_path)
    key = '{}/config/ssl/farmer/private_farmer.key'.format(chia_root_path)
    return make_request(url, cert, key)


@api.route('/get_harvester_plots_invalid', methods=['GET'])
def get_harvester_plots_invalid():
    url = 'https://localhost:8559/get_harvester_plots_invalid'
    cert = '{}/config/ssl/farmer/private_farmer.crt'.format(chia_root_path)
    key = '{}/config/ssl/farmer/private_farmer.key'.format(chia_root_path)
    return make_request(url, cert, key)


@api.route('/get_harvester_plots_keys_missing', methods=['GET'])
def get_harvester_plots_keys_missing():
    url = 'https://localhost:8559/get_harvester_plots_keys_missing'
    cert = '{}/config/ssl/farmer/private_farmer.crt'.format(chia_root_path)
    key = '{}/config/ssl/farmer/private_farmer.key'.format(chia_root_path)
    return make_request(url, cert, key)


@api.route('/get_harvester_plots_duplicates', methods=['GET'])
def get_harvester_plots_duplicates():
    url = 'https://localhost:8559/get_harvester_plots_duplicates'
    cert = '{}/config/ssl/farmer/private_farmer.crt'.format(chia_root_path)
    key = '{}/config/ssl/farmer/private_farmer.key'.format(chia_root_path)
    return make_request(url, cert, key)


@api.route('/get_plots', methods=['GET'])
def get_plots():
    url = 'https://localhost:8560/get_plots'
    cert = '{}/config/ssl/harvester/private_harvester.crt'.format(chia_root_path)
    key = '{}/config/ssl/harvester/private_harvester.key'.format(chia_root_path)
    return make_request(url, cert, key)


def make_request(url, cert, key):
    context = (cert, key)
    response = requests.post(url, data='{}', headers=headers, cert=context, verify=False)
    return response.json()


@click.command()
@click.option('--chia_root', '-c', default='')
def main(chia_root):
    global chia_root_path
    chia_root_path = chia_root
    api.run()


if __name__ == '__main__':
    main()
