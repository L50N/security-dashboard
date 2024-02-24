
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
    checkLogin() {
      axios.get('http://localhost:5000/check-login', { withCredentials: true })
          .then(response => {
            if (!response.data.loggedIn) {
              this.$router.push('/');
            } else {
              console.log('Login could be verified.')
            }
          })
          .catch(error => {
            console.error('Error checking login status:', error);
            this.$router.push('/');
          });
    }
  }
}
</script>