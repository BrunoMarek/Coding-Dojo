var likes = [9, 12, 9];
var spans = [
    document.querySelector("#like1"),
    document.querySelector("#like2"),
    document.querySelector("#like3")
];

function like(id) {
    likes[id]++;
    spans[id].innerHTML = likes[id] + "like(s)";
}