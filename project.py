from bigchaindb_driver import BigchainDB
from bigchaindb_driver.crypto import generate_keypair
from time import sleep
from sys import exit

def asset_creation(farmer, tomatos, tomatos_metadata, bdb):
	prepare_cr_tx = bdb.transactions.prepare(
		operation = 'CREATE', 
		signers = farmer.public_key, 
		asset = tomatos, 
		metadata = tomatos_metadata
	)

	fulfilled_cr_tx = bdb.transactions.fulfill(
		prepare_cr_tx, 
		private_keys = farmer.private_key
	)

	sent_cr_tx = bdb.transactions.send_commit(fulfilled_cr_tx)

	print("Creation done (status): ",fulfilled_cr_tx == sent_cr_tx)
	return sent_cr_tx


def asset_transfer(fulfilled_cr_tx, buyer, farmer, bdb):
	transfer_asset = {'id':fulfilled_cr_tx['id']}
	output = fulfilled_cr_tx['outputs'][0]

	transfer_input = {
		  'fulfillment': output['condition']['details'],
		  'fulfills': {
		  	'output_index': 0,
		    'transaction_id': fulfilled_cr_tx['id']
		  },
		  'owners_before': output['public_keys']
	}


	prepared_transfer_tx = bdb.transactions.prepare(
		  operation='TRANSFER',
		  asset=transfer_asset,
		  inputs=transfer_input,
		  recipients=buyer.public_key,
	)

	fulfilled_transfer_tx = bdb.transactions.fulfill(
		  prepared_transfer_tx,
		  private_keys=farmer.private_key,
	)

	sent_transfer_tx = bdb.transactions.send_commit(fulfilled_transfer_tx)
	print("Transfer done (status): ", fulfilled_transfer_tx == sent_transfer_tx)
	return sent_transfer_tx

def run(tomato, tomato_metadata, farmer, buyer, bdb):
	fulfilled_cr = asset_creation(farmer, tomatos,tomatos_metadata, bdb)
	sent_trans = asset_transfer(fulfilled_cr, buyer, farmer, bdb)
	#print("Is Buyer the owner?",
		#  sent_transfer_tx['outputs'][0]['public_keys'][0] == farmer.public_key)
		
if __name__ == '__main__':
	bdb = BigchainDB("https://test.bigchaindb.com")
	farmer, trader, buyer = generate_keypair(), generate_keypair(), generate_keypair()
	
	while(input("Press q (quit) to stop ") != 'q'):
		tomatos = {
						'data': {
							input("Product name: ") : {
								'price_euros' : float(input("Product price: ")), 
								'quantity_kilos': float(input("Product quantity: "))
							},
						},
					}
		tomatos_metadata = {'plant' : 'farm'}
		run(tomatos, tomatos_metadata, farmer, buyer, bdb)
		
