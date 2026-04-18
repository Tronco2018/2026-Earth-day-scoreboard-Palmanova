const colours = ["#B59410", "#aaaaaa", "#a97142"];
const medals = ["🥇", "🥈", "🥉"];

function change_colours() {
    classifica_div = document.getElementById("classifica").querySelectorAll("div");
    max_val = classifica_div.length;
    for (var i = 0; i < max_val; i++) {
        console.log(classifica_div[i])
        classifica_div[i].style.backgroundColor = colours[i];
        var s = i + 1
        classifica_div[i].querySelectorAll("span")[0].innerText = (i > 2 ? "" : medals[i]) + s + ". ";
    }
    
}

fetch("../scores.json")
    .then(res => res.json())
    .then(data => {
        // Sorting data
        data.sort((a, b) => b.score - a.score);

        // Build HTML
        const html = data.map((item, index) => {
            return `
                <div class="elemento_class">
                    <span id="num">${index + 1}.</span> <span id="num">${item.name}</span> - <span id="num">${item.score}</span>
                </div>
            `;
        }).join("")
 
        // Insert in document
        document.getElementById("classifica").innerHTML = html;

        change_colours();
    })


