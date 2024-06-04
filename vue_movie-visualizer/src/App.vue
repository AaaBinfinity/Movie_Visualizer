<template>
  <div id="app" class="container">
    <header class="my-4 text-center">
      <h1>Movie Visualizer</h1>
    </header>
    <div class="row">
      <div class="col-md-6">
        <PieChart />
      </div>
      <div class="col-md-6">
        <BarChart />
      </div>
    </div>
  </div>
</template>

<script>
import PieChart from './components/PieChart.vue';
import BarChart from './components/BarChart.vue';

export default {
  name: 'App',
  components: {
    PieChart,
    BarChart,
  },
};
</script>

<style>
#app {
  background-color: #f8f9fa;
  padding: 20px;
  border-radius: 10px;
}

header h1 {
  color: #343a40;
}

.row {
  margin-top: 20px;
}
</style>
