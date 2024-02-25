
import Current from './components/current.vue';
<template>
  <div>
    <LazyNuxtPage />
  </div>
</template>

<script>
import axios from 'axios';

export default {
  name: 'App',
  created() {
    this.checkLogin();
  },
  methods: {
    async checkLogin() {
      try {
        const response = await axios.get('http://localhost:5000/check-login', { withCredentials: true });
        if (response.data.logged_in) {
          console.log('User is logged in');
        } else {
          console.log('User is not logged in');
        }
      } catch (error) {
        console.error('Error checking login status:', error);
      }
    }
  }
}
</script>
