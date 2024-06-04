<template>
    <div class="card">
      <div class="card-body">
        <h2 class="card-title">Bar Chart</h2>
        <img :src="barChartUrl" alt="Bar Chart" class="img-fluid">
      </div>
    </div>
  </template>
  
  <script>
  export default {
    data() {
      return {
        barChartUrl: 'http://127.0.0.1:5000/api/genres/bar-chart',
      };
    },
  };
  </script>
  