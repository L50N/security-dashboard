<template>
    <div class="space-y-1 max-w-[744px]">
        <p class="text-primary font-medium">All the important informations, you need.</p>
        <p class="text-4xl font-semibold">Dashboard</p>
        <p class="text-gray-500">sit amet facilisis magna etiam tempor orci eu lobortis elementum nibh tellus molestie nunc non blandit massa enim nec dui nunc mattis enim ut tellus</p>

      <div>
        <button @click="makeRequest">Make Request</button>
      </div>
    </div>
</template>

<script>
import axios from 'axios';

export default {
  methods: {
    makeRequest() {
      axios.get('http://localhost:5000/')
          .then(response => {
            console.log(response.data);
          })
          .catch(error => {
            console.error('Error:', error);
          });
    }
  }
}
</script>