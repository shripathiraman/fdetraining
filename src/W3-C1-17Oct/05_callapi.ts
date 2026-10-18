//call an api

async function getPlaceHolder() {
    const response = await fetch("https://jsonplaceholder.typicode.com/posts/")
    //return response;
    console.log(response.ok)
    console.log(response.status)
    console.log(response.statusText)
    console.log(response.headers)
    console.log(response.url)
    console.log(response.type)
    console.log(response.redirected)
    console.log(response.body)
    console.log(await response.json())
}

//const response = await getPlaceHolder();
//console.log(await getPlaceHolder());
getPlaceHolder();