var NameSub = document.getElementById("sub_username");
var NameWords = document.getElementById("username");
NameSub.onclick = function () {
    if (NameWords.value == "") {
    alert("please input your name!");
} else
    {
    alert("welcom " + NameWords.value + "!");
    }
}
