<template>
    <div class="card">
      <div class="card-body">
        <h2 class="card-title">Pie Chart</h2>
        <img :src="pieChartUrl" alt="Pie Chart" class="img-fluid">
      </div>
    </div>
  </template>
  
  <script>
  export default {
    data() {
      return {
        pieChartUrl: 'http://127.0.0.1:5000/api/genres/pie-chart',
      };
    },
  };
  </script>
  