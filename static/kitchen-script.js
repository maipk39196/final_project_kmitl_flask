const today = new Date();
const day = String(today.getDate()).padStart(2, '0');
const month = String(today.getMonth() + 1).padStart(2, '0');
const year = today.getFullYear();
const currentDate = `${year}-${month}-${day}`;
document.getElementById('datePicker').value = currentDate;

function calculateTotal() {
    let total = 0;
    const prices = document.querySelectorAll('#reportTable tbody td:last-child');
    prices.forEach(price => {
        total += parseFloat(price.textContent);
    });
    document.getElementById('totalPrice').textContent = total;
}

calculateTotal();