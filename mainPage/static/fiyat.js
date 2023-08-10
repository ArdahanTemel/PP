
const field1 = document.getElementById('miktar');
const field2 = document.getElementById('hurda');
const field3 = document.getElementById('birimFiyat');
const field4 = document.getElementById('odenecek');

field1.addEventListener('input', updateField4);
field2.addEventListener('input', updateField4);
field3.addEventListener('input', updateField4);

function updateField4() {
const val1 = Number(field1.value);
const val2 = Number(field2.value);
const val3 = Number(field3.value);
field4.value = (val1 - val2) * val3;
}
