function updateCart (btn){
    if (!btn.hasAttribute("data-disabled")){
        btn.setAttribute("data-disabled", "")
        let url = "/store/update_cart/",
        action = btn.dataset.action,
        productID,
        quantity;

        switch (action) {
            case "add-item":
                productID = btn.dataset.id;
                quantity = document.getElementById("quantity").value;
                break;
            case "remove-item":
                productID = btn.dataset.id;
                quantity = "";
                break;
            case "remove-cart":
                productID = "";
                quantity = "";
                break;
        }
        fetch(url, {
            method: "POST",
            mode: "same-origin",
            headers: {
                "Content-Type": "application/json",
                "X-CSRFToken": csrftoken
            },
            body: JSON.stringify({"productID": productID, "action": action, "quantity": quantity})
        })
            .then(() => {
                if (action === "add-item"){
                    location.href = "/store/cart/"
                } else {
                    location.reload()
                }
            })

    }
}