<template>
  <div>
  </div>
</template>

<script>
export default {
  async asyncData({ error }) {
    error({ statusCode: 302, message: 'Redirecting...' });
  },
  mounted() {
    this.$router.push('/');
  },
};
</script>
