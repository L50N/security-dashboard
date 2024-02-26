
import Current from './components/current.vue';
<template>
  <div>
    <LazyNuxtPage />
  </div>
</template>

<script>
import Current from './components/current.vue';

export default {
  components: {
    Current
  },
  async mounted() {
    const response = await fetch('http://localhost:5000/check-login', {
      method: 'GET',
      credentials: 'include'
    });
    const data = await response.json();
    
    if (!data.logged_in) {
      this.$router.push('/');
    }
  }
}
</script>