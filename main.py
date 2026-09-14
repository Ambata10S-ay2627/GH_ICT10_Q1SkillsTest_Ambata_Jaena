# Receipt Generator
from pyscript import display, document


def create_order(e):
    prod1 = document.getElementById("item1")
    prod2 = document.getElementById("item2")
    prod3 = document.getElementById("item3")
    prod4 = document.getElementById("item4")

    subtotal = float(prod1.value) * prod1.checked + float(prod2.value) * prod2.checked + float(prod3.value) * prod3.checked + float(prod4.value) * prod4.checked
    display(subtotal, target="show")
    display(f'Your subtotal {subtotal}', target="show")

    
    vAT = subtotal * 0.12
    display(f'Your vAT {vAT}', target="show")
    
    total_amount = subtotal + vAT
    display(f'Your total amount {total_amount}', target="show")
