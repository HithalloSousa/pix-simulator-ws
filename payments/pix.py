import uuid
import qrcode

class Pix:
    def __init__(self):
        pass
    
    def create_payment(self):
        # Criação do pagamento na instituição financeira
        bank_payment_id = str(uuid.uuid4())
        
        # Metodo Copia e Cola Qr_Code
        hash_payment = f'hash_payment_{bank_payment_id}'
        
        # Criação do QR_Code
        img = qrcode.make(hash_payment)
        # Salva a imagem como arquivo PNG
        img.save(f"static/img/qr_code_payment_{bank_payment_id}.png")
        
        return {
            "bank_payment_id": bank_payment_id,
            "qr_code_path": f"qr_code_payment_{bank_payment_id}"
        }