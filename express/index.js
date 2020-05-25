// window.onload() => {
  $.get('http://localhost:4000/rawdata/', {}, (data)=>{
    // console.log(data['GA']);
    // console.log(data['PSO']);
    document.getElementById('ga-x').innerHTML = data['GA']['x'];
    document.getElementById('ga-fx').innerHTML = data['GA']['fx'];
    document.getElementById('pso-x').innerHTML = data['PSO']['x'];
    document.getElementById('pso-fx').innerHTML = data['PSO']['fx'];
  });
// }
