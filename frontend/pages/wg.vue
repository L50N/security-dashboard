<script setup lang="ts">
const route = useRoute()
</script>

<template>
  <div>
      <Sitebar />
      <div class="pl-[324px] pr-12 pt-7">
        <Current />
      </div>
      <div class="pl-[324px] pr-12 pt-[56px]">
        <wgAdd />
        <wgHero />
        <wgStatistics />
        <Separator />
        <wgProfiles />
      </div>
  </div>
</template>
