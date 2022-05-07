async function init() {
  const aux = await fetch("../data/data.json")
    .then((response) => {
      return response.json();
    })
    .then((jsondata) => {
      return jsondata;
    });
  //console.log(aux);
  return aux;
}
