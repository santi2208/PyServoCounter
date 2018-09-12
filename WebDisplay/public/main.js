var viewModel;

var socket = io.connect('http://localhost:8012', { 'forceNew': true });

socket.on('estadosServos', (servos) =>{
  console.log(servos);
  BuildViewModel(servos);
})

//-------------------Building--------------------
function BuildViewModel(servos)
{
  debugger;
  var servosmodels = [];
  var ctr = 1;
  servos[1].forEach(function(state) {
    servosmodels.push(new ServoViewModel(ctr, state));
    ctr += 1;
  });
  
  viewModel.Number(new NumberViewModel(servos[0], servosmodels));
  // viewModel.Servos(servosmodels);
}

//--------------------ViewModels-----------------
var ServoViewModel=function(id, state){
  var self = this;
  self.Id = ko.observable(id);
  self.State = ko.observable(state);
}

var NumberViewModel = function(numberId, servos){
  var self = this;
  self.Id = ko.observable(numberId);
  self.Servos = ko.observableArray(servos);
}

var ViewModel = function(number)
{
  var self = this;
  self.Number = ko.observable(number);
}

//--------------------Load-----------------
$(() => {
  //General Viewmodel
  viewModel = new ViewModel([]);
  ko.applyBindings(viewModel);
});