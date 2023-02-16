let updateButtons = document.getElementsByClassName("update-cart")

for (let i = 0; i < updateButtons.length; i++) {
    updateButtons[i].addEventListener('click', function(){
        let productId = this.dataset.product
        let action = this.dataset.action
        console.log('productId: ', productId, 'action: ', action)
        console.log('user: ', user)
        if (user === 'AnonymousUser') {
            console.log('Not Logged in')
        } else {
            updateUserOrder(productId, action)
        }
    });
}

function updateUserOrder(productId, action) {
    console.log('User is authenticated, sending data..')
    let url = '/update_item/'
    fetch(url, {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json',
            'X-CSRFToken': csrftoken,
        },
        body: JSON.stringify({'productId': productId, 'action': action })
    })
        .then((res) => {
            return res.json()
        })
        .then((data) => {
            console.log(data)
            location.reload()
        })
}