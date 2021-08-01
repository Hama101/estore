    let search_form = document.getElementById("search-form")
    let buttons = document.getElementsByClassName("page-link")

    if(search_form){
        for (let i = 0 ; buttons.length ; i++){
            buttons[i].addEventListener('click' , function (e){
                e.preventDefault()
                let page = this.dataset.page
                search_form.innerHTML += `<input type="hidden" hidden name="page" value=${page}>`
                search_form.submit()
            })
        }
    }