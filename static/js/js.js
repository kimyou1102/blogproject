const delete = doqument.querySelector(".delete");

function handleClick() {
    if(!confirm("삭제하면 다시 복구할 수 없습니다. 삭제하시겠습니까?")) {
        alert("취소(아니오)를 누르셨습니다.");
    } else {
        alert("확인(예)를 누르셨습니다.");
    }
}

window.addEventListener("click", handleClick())