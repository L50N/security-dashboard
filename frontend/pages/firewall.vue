<script setup lang="ts">
import { ref } from 'vue';
import { useRouter } from 'vue-router';

const router = useRouter();
const loggedIn = ref(false);

const checkLoginStatus = async () => {
  try {
    const response = await fetch('http://localhost:5000/check-login', {
      method: 'GET',
      credentials: 'include'
    });
    const data = await response.json();
    loggedIn.value = data.logged_in;
    if (!loggedIn.value) {
      router.push('/');
    }
  } catch (error) {
    console.error('An error occurred while checking login status:', error);
  }
};

import { onMounted } from 'vue';
onMounted(checkLoginStatus);
</script>

<template>
  <div v-if="loggedIn">
      <Sitebar />
      <div class="pl-12 xl:pl-[324px] pr-12 pt-9">
        <Current />
      </div>
      <div class="pl-12 xl:pl-[324px] pr-12 pt-[56px]">
        <firewallHero />
        <IndexStatistics />
      </div>
  </div>
</template>
