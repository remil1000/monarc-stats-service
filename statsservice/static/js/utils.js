// define some colors for the lines of the chart
chartColors = [
  'rgba(230, 25, 75, 0.8)',
  'rgba(60, 180, 75, 0.8)',
  'rgba(255, 225, 25, 0.8)',
  'rgba(0, 130, 200, 0.8)',
  'rgba(245, 130, 48, 0.8)',
  'rgba(145, 30, 180, 0.8)',
  'rgba(70, 240, 240, 0.8)',
  'rgba(240, 50, 230, 0.8)',
  'rgba(210, 245, 60, 0.8)',
  'rgba(250, 190, 190, 0.8)',
  'rgba(0, 128, 128, 0.8)',
  'rgba(230, 190, 255, 0.8)',
  'rgba(170, 110, 40, 0.8)',
  'rgba(255, 250, 200, 0.8)',
  'rgba(128, 0, 0, 0.8)',
  'rgba(170, 255, 195, 0.8)',
  'rgba(128, 128, 0, 0.8)',
  'rgba(255, 215, 180, 0.8)',
  'rgba(0, 0, 128, 0.8)',
  'rgba(128, 128, 128, 0.8)',
  'rgba(0, 0, 0, 0.8)'
];


// basic configuration of the charts (threats and vulnerabilities)



var config_base_bar_chart_informational_risks = {
  type: 'bar',
  data: {
    labels: ["Low", "Medium", "High"],
    datasets: []
  },
  options: {
    legend: { display: true },
    title: {
      display: true,
      text: 'Informational risks'
    }
  }
};


var config_base_bar_chart_operational_risks = {
  type: 'bar',
  data: {
    labels: ["Low", "Medium", "High"],
    datasets: []
  },
  options: {
    legend: { display: true },
    title: {
      display: true,
      text: 'Operational risks'
    }
  }
};


let retrieve_information_from_mosp = function(uuid, language) {
  return new Promise(function(resolve, reject) {
    fetch("https://objects.monarc.lu/api/v2/object/?language="+language+"&uuid="+uuid, {
      method: "GET",
      headers: {
        'Content-Type': 'text/plain',
      },
    })
    .then((resp) => resp.json())
    .then(function(mosp_result) {
      if (mosp_result["metadata"].count > 0) {
        resolve(mosp_result["data"][0].name);
      } else {
        resolve();
      }
    })
    .catch((error) => {
      console.error('Error:', error);
      reject(Error(error));
    });;
  });
}

let mosp_lookup_by_label = function(label) {
  return new Promise(function(resolve, reject) {
    fetch("https://objects.monarc.lu/api/v2/object/?page=1&per_page=10&name="+label, {
      method: "GET",
      headers: {
        'Content-Type': 'text/plain',
      },
    })
    .then((resp) => resp.json())
    .then(function(mosp_result) {
      if (mosp_result["metadata"].count > 0) {
        resolve(mosp_result["data"][0].json_object.uuid);
      } else {
        resolve();
      }
    })
    .catch((error) => {
      console.error('Error:', error);
      reject(Error(error));
    });;
  });
}

let let_pie_charts_modals = function(object_uuid) {
  if (object_uuid) {
    MOSPModal.show()
    document.getElementById("MOSPModalClose").onclick = function(){
    };
    document.getElementById("MOSPModalOK").onclick = function(){
      window.location = 'https://objects.monarc.lu/object/'+object_uuid;
    };
  } else {
    unknowObjectModal.show();
  }
}
