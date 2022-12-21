function hobby1() {
    hobby1_dropdown = document.getElementById("hobby1");
    hobby1_dropdown.onchange = (ev) =>{
        let selected = hobby1_dropdown.options[hobby1_dropdown.selectedIndex];
        return selected.text;
    }
}

function hobby2() {
    hobby2_dropdown = document.getElementById("hobby2");
    hobby2_dropdown.onchange = (ev) =>{
        let selected = hobby2_dropdown.options[hobby2_dropdown.selectedIndex];
        return selected.text;
    }
}
