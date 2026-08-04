function changeContent(button_clicked) {
    const buttons = document.querySelectorAll('.btn-tab');
    buttons.forEach(button => {
        button.classList.remove('activated');
    })

    button_clicked.classList.add('activated');

    const contents = document.querySelectorAll('.tab-content');
    contents.forEach(content => {
        content.classList.remove('active');
    })

    const tabId = button_clicked.dataset.tab;
    document.getElementById(tabId).classList.add('active');
}

function showResumo(button_clicked, name, description, url){
    const buttons = document.querySelectorAll('.btn-project');
    buttons.forEach(button => {
        button.classList.remove('looking');
    })

    button_clicked.classList.add('looking');

    const h2 = document.getElementById('project-name');
    const p = document.getElementById('project-description');
    const a = document.getElementById('project-url');

    h2.textContent = name;

    if (description === "None" || description === null || description === ""){
        p.textContent = "Esse projeto não possui uma descrição.";
    } else {
        p.textContent = description
    }
    
    a.href = url;
    a.textContent = "Acessar Projeto: " + url;
}