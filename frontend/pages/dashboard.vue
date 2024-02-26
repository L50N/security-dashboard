<script setup lang="ts">
import { ref } from 'vue';

const loggedIn = ref(false);
(async () => {
  try {
    const response = await fetch('http://localhost:5000/check-login', {
      method: 'GET',
      credentials: 'include'
    });
    const data = await response.json();
    loggedIn.value = data.logged_in;
  } catch (error) {
    console.error('An error occurred while checking login status:', error);
  }
})();
</script>


<template>
  <div v-if="loggedIn">
    <Sitebar />
    <div class="pl-12 xl:pl-[324px] pr-12 pt-7">
      <Current />
    </div>
    <div class="pl-12 xl:pl-[324px] pr-12 pt-[56px]">
      <dashboardHero />
      <dashboardStatistics />
    </div>
  </div>
</template>
