<script setup lang="ts">

</script>

<template>
  <div class="ml-64 p-6 select-none">

      <!-- SEARCHBAR CONTAINER -->
      <div class="grid grid-cols-[2fr,1fr,80px,80px,80px] 2xl:grid-cols-[3fr,1fr,80px,80px,80px] space-x-3">
      <div class="bg-white rounded-2xl text-xl px-12 flex flex-row items-center">
        <p class="text-gray-400">Search</p>
        <div class="flex justify-end w-full">
        <svg width="24" height="24" viewBox="0 0 19 19" fill="none" xmlns="http://www.w3.org/2000/svg" xmlns:xlink="http://www.w3.org/1999/xlink">
        <rect width="19" height="19" fill="url(#pattern0)"/>
        <defs>
          <pattern id="pattern0" patternContentUnits="objectBoundingBox" width="1" height="1">
            <use xlink:href="#image0_9_867" transform="scale(0.0111111)"/>
          </pattern>
          <image id="image0_9_867" width="90" height="90" xlink:href="data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAAFoAAABaCAYAAAA4qEECAAAACXBIWXMAAAsTAAALEwEAmpwYAAAFhUlEQVR4nO2cy28cRRDGGyTCI+TAG64oggMoSLxBIHKIEpBAAf4OIL6BuRghJLgQ7ABXZIVHkpEQm9XM9/XgVRYQ4RH5CIFLgERJMJj4woHYCBYVbiPLTPfuOvZ097h/UkvW2p6t+ba3urq6apRKJBKJRCKRSCQSicT/KctyM8ldJEdJTpL8iuQJknMk582YM699af5mFMDOdrt9RcUlE0uUZXk9gBEAnxkhe6sc8+Yae+Sa/73BRofkwwAOA/jzAsStHAAWzLUfUhsVAI+Q/HStxXWMT+RDVRuFPM9vBLAfwN81irx8ZJ1O5wbVZEg+bRaxnucxVxTFk6ppZFm2CcDEMLMYwFkA7wN4VqIJrfXWPM+vmp6evkSG/Cyvye9IPid/S/LnIa4vtrwh11JNoNvtXgng4wEF+BXAeFmWd632/YqiuFs+VJKzAwquxUYVM1NTU9eQPDbAzZ7UWj+TZdnla/Xeci3zbTg1wPt/LbaqGJGNA4AvBgi/JtZzRongJF8ieb6P4Meim9nGJ/dzF9+SvK0um8qyvJ3k8X5uJCqfbXykS+QDPrbK5eLWPutj214VAwCecEUXAN4aGxu72Jd9vV7vIgCvu6IRAE+p0DcjfeLkfSoQALzpEPtc0HkSku+63IXPmbwSsaWPG5lUoeYubC4DwDchpi+7izH+dw4XEl4yypEgOl9ndDEsALbZ0rIAjqiQIPmAw9+9rAKH5KsO+8OZ1ZLzte341nK3t85h32mL2B+pgE5GFqqMlG21igQAI47d63XBGigJohhm8xKyWNsSUZIzUb4x53NVxo2ryCC5z3Iv3RB8m+0g9U4VGQDusUVOXr+dJuleNQPOqgjpLW7PZyxi7/BmGMkXLUa9pyKF5AHL5Hnep1GTwS4eq0TqQSz39I7yhakSqjJqp4oUrfWjlns66s0oAD9WGZXn+c0qUrTWWy1C/+DNKEknWjYqV6u4zzl7FWPWm1G20E6OslSkZFm2yRbieTOqiUIDuNQi9LxPoxrnOtrt9rUWH33Om1EbbDE8GVx4J0XkKlKKonjMck+fB7dhkVo4FSmwp0v3ezPKtD5UGfWBihSSBy2TZ9SnUbssQs9IgkY1K6m03XeyvDLEk6pOFRl5nt9nmTgLkhIONfE/oSID9qKaTrDZLjnKCrGWo0/162/Bnn26DmdjSpfCcThL8iYVeLnBqRhmdVmWmwGcsdzDIRUKUmRicR8yXlGBQ/K1KApoBNPHV5n1kiJwFSha6zscB8z+F0FLB6ytLvq49/CoglartQXA944ix/tViMg21eFCstDKdgF8GF3ZriAdqa5CdIlTVSCQfNsh8qykS1XIaK0fj721ooilq1Y6Uh2z5V834qPVrLXok13uIp5mIUFayKSVzHVDUmkPYFud0YVt4VsxCjnOUpFtaY8O0tDZarW2rKcdAzZ0rmxbvkzFdHQv7b8D3NxpyZms5S7SfNAjth1f42a2achxuhEuW+2ldFZrfe9q8tnyP5LqlOjGliBqtNjis2WRGfIxEjOm4HCPlGkVRXGLPDpCShlkyEk7yVvldyYhdBDAL0NcX2zZK2I2SmyB5G5biQLrHfLN2b2sjqN5YstMNL3if3kSOVvZk2IeEnC4UQvkEpIVA3CkRoE7rtxFY2f2ElrrB6XFzHZ4cCHDhI+HBk11Nl5sQXIL5okx3WFi3gpx5fl5HTl+Ws3JyIYQe8VTY3YAeEEq7c2TbE6YhXTezH5JXv0kFUQmayg1JtvXIh07oNhohNi+afQCGRpJ7PoL09tpZtdAErtGktg1ksSuERP6IYV+gYgd49MdohQbwO8x1ohHJzaAP0KqY2ms2F6b9JssNoBxcRcyk0Xk6J7cGxPik5NfTiQSiUQikUgk1LrzD0i1kExWkB8VAAAAAElFTkSuQmCC"/>
        </defs>
      </svg>
      </div>
      </div>

      <!-- TIME-FRAME SETTING -->
      <div>
        <div class="bg-white rounded-2xl txt-xl py-5 px-8 grid grid-cols-[1fr,18.5px] flex-row items-center">
          <div>
          <p class="text-gray-400 w-full text-lg">Last 2 months</p>
          </div>
          <div class="flex justify-end w-full">
            <svg xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 24 24" stroke-width="1.5" stroke="currentColor" class="stroke-gray-400">
              <path stroke-linecap="round" stroke-linejoin="round" d="M13.5 4.5L21 12m0 0l-7.5 7.5M21 12H3" />
            </svg>

          </div>
        </div>
      </div>

      <!-- FILTER OPTION -->
      <div class="bg-white rounded-2xl">
        <div class="flex justify-center items-center h-full w-full cursor-pointer">
          <svg xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 24 24" stroke-width="1.5" stroke="currentColor" class="w-7 h-7">
            <path stroke-linecap="round" stroke-linejoin="round" d="M12 3c2.755 0 5.455.232 8.083.678.533.09.917.556.917 1.096v1.044a2.25 2.25 0 01-.659 1.591l-5.432 5.432a2.25 2.25 0 00-.659 1.591v2.927a2.25 2.25 0 01-1.244 2.013L9.75 21v-6.568a2.25 2.25 0 00-.659-1.591L3.659 7.409A2.25 2.25 0 013 5.818V4.774c0-.54.384-1.006.917-1.096A48.32 48.32 0 0112 3z" />
          </svg>
        </div>
      </div>

        <!-- WARNINGS ON ACCOUNT -->
        <div class="bg-white rounded-2xl cursor-pointer">

          <!-- RED INFO POINT -->
          <div class="h-[0.85rem] w-[0.85rem] rounded-full absolute bg-red-400"></div>

          <div class="flex justify-center items-center h-full w-full">
            <img src="../public/Warning.svg" class="w-8 h-8">
          </div>
        </div>

      <!-- PROFILE IMAGE -->
      <div class="rounded-2xl">
        <div class="flex justify-center items-center h-full w-full">
         <img class="rounded-2xl" src="../public/92170476.png">
        </div>
      </div>
    </div>
  </div>
</template>

<style scoped>

</style>