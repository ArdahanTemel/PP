function calculateDifferences() {
  var num1 = parseInt(document.getElementById("w1").value);
  var num2 = parseInt(document.getElementById("w2").value);
  var num3 = parseInt(document.getElementById("w3").value);
  var num4 = parseInt(document.getElementById("w4").value);
  var num5 = parseInt(document.getElementById("w5").value);
  var num6 = parseInt(document.getElementById("w6").value);

  var diff1 = num2 - num1;
  var diff2 = num3 - num2;
  var diff3 = num4 - num3;
  var diff4 = num5 - num4;
  var diff5 = num6 - num5;

  document.getElementById("weigh1").textContent = "Difference 1: " + diff1;
  document.getElementById("weigh2").textContent = "Difference 2: " + diff2;
  document.getElementById("weigh3").textContent = "Difference 3: " + diff3;
  document.getElementById("weigh4").textContent = "Difference 4: " + diff4;
  document.getElementById("weigh5").textContent = "Difference 5: " + diff5;
}
