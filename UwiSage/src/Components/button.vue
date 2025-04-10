<template>
  <button class="custom-button">
    {{ text }}
  </button>
</template>

<script>
export default {
  props: {
    text: String
  }
}
</script>

<style>
.custom-button {
  background: blue;
  color: white;
  padding: 10px;
  border-radius: 5px;
}
</style>
