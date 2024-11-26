<template>
    <div>
      <!-- Company Watermark -->
      <div class="watermark sysbar">
        <div class="items-container">
          <i class="icon icon-econ"></i>
          <div class="product">
            SOS app <br />
          </div>
        </div>
      </div>
  
      <!-- Footer -->
      <div class="footer">
        © Ericsson AB 2013-{{ new Date().getFullYear() }} - All Rights Reserved.
        <br />
        No part of this software may be reproduced in any form without the
        written permission of the copyright holder.
      </div>
    </div>
  </template>
  
  <style scoped>
  /* Watermark Styles */
  .watermark {
    position: absolute;
    top: 20px;
    left: 20px;
    opacity: 0.8;
    pointer-events: none;
  }
  
  .watermark .sysbar .items-container .icon.icon-econ {
    font-size: 21px;
    color: #fff; /* White icon */
  }
  
  .watermark .product {
    font-size: 14px;
    font-weight: bold;
    text-transform: uppercase;
  }
  
  /* Footer Styles */
  .footer {
    text-align: center;
    padding: 20px;
    background: #111;
    color: #d7cfcf; /* White text */
    border-top: 1px solid #333;
    font-size: 14px;
    position: absolute;
    bottom: 0;
    width: 100%; /* Full-width footer */
  }
  </style>
  