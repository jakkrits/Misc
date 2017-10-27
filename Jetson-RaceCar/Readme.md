# Jetson RACECAR
This repo is my personal note of detailed instruction on building Jetson RACECAR which is based on [Jim's website](JetsonHack.com "JetsonHack").

# What you'll need
1.  __NVidia Jetson TX1 or TX2__ (This project uses the TX1) ![TX1](https://lh3.googleusercontent.com/-TOI_46PsFoKAcSM5zysTRYzy_a4bW9tpEVzjkNpOIsVjl8pWM067rEZzpwjWyAKUAYg8OGRMEzFQSB1ly0wGIFgf6NcRWp37t57MRJCoLJVQfWOB8cAhFnLeEYSiprWOH3gYBVt2eEAtGBpgZXIyHvAQOu42jt8qHD7Nl6mjdfy2Qs872iwscHVRRLHpSGFYk1lWhHGD4Y41dXtgYkGdcjZjdi_SWZjjgInB2Oe6EEtQL8CtT1jCSDTTVfRNnETpUv08OCs6JQJhG6Ianj_-EsLvq7br6rynUamy32xl_UPPyT0cXHRr0P0U3gW5pUmwh9kSFjuZkwf5rTJkLFfpdAdkYG6wOu1LchaOEjYk7HjUFWppR2pgcPAGDyCQgMAH3RBNw-Vm40OVASL-K_MYmTD1qcWP7I0UB4il-m9WEXPssXhNghHO7oTMEnoTqnP1bhnLYCmi4Nx-qBePFWYICF-ez_db8CuQvcwJw2vUYlAccf3x7AAdrZPh336oB9RGsdHXVPq98heZdVJdAXGRsgdJPIJ7Ts7kLw9sor53tL1871RrfILchH7YLyH3_wtaifjxClKOv_qGgcmwADU7abRyjLRn_E9Yhn4yZPDMGw=w1668-h1250-no)

2. __Zed Camera__ ![Zed](https://lh3.googleusercontent.com/YDESm3kzCvUU7fOc7Oj9mnj3ARHW6QlP45Mx7aEdqP2V_nB6IrrenWJS-LCRAbjHVHlTes9MGXZvHOAw1SpLxrlZfYLiA-iKthXtymSXXI9J5gn72Czaz-f1FyiKnoRCH1xDcUGtI1PQN9qk6CzrwPAs2EroHqNaVIdn5A14e7-TApHoKB8PuPW1k7AtyfPMFSrQiAuOGz5qvcqc2eF_WR3cLmJ4hUhBcThSJntW8pHJFK_wLudn3krKl1A4nvbJQgLX8bLP2S7aeBD02KsXaKovbdaIYfpUI2V6wImSZknnyY4KXaDZ74Z1eNP8uoFPnAaJeftRn2WGx3qc0L7kBvvD2_sTHw3eX6GauOuH7NxzBLyHMMXAWucGBKaYSa1jgyY2mqmVo22QAZP1JGyzZF4GBKkkR35P_OXLOgupHg1sYiq531LVe1DZqT7kTJChxgi2RH7QAv1MOUq4oTLTUGuKjFscFHKq-J6Tt5FZ9wcaWaZz9Pu0gGMov0GhdD_9iqqNOjREarw4Vdukgi2CDEKWrFazg6SUzglS9pP-MRqDP9ntrTryR0m92Pyb-3yJg1A2FAUqaA65cTYA2NXpuZbOJ0KBeBR7Mk5HH-frvVc=w938-h1250-no)

3. __Amazon Basics USB Hub or else__ ![Amazon Hub](https://lh3.googleusercontent.com/KTmCTYVtA-Yd_BI2sTt6wR-0kJcVKrYKYG-gKaDZdhtUYmD1XeDH2RlBe47RYAsAPdqcLMHCAqBXT8BFX9WJYTv3eZV049nBXcUwFAnkxWOTL9S8DhoYI5YNzpaqaXgiIAOoA7tnSPCthouCEc2gjKHsxcx7joQRa9Qg6oMbZhzvYoqoooHNCktJQeoF3VEYvDF4f9oFPMeUs6PouXuTl3RG7tegjXhs63S4aP7m8K_G5mv3JSxzQVE04xITmT4jI24ip77LY04LD3rgXLISw5jVvC0kPF_oumH6osB8yiNfn28Ymr3WmyMHCXN0t1iw2ma_Iel_jHupMbVfhkC-v1VM5ZFf-PfzmkEOQv6SpbNVxZ5s7XkOy5VGpuvonWLunNLm4R17f7VsyMX8ezzZJpHu5tAlZ_cBb36nN-xAXDzWGw2WnnVisfMuAvqfTzTO5BLYEMemova_xzVbtAh314A4JDWNCLzG2byjulWqze66cmfhTJpXiCse_e4fwYuxX4eSh8BAElRbYptKOSF7TzzVL98DoS5kpjDfMHmbLWb-pEsNBNMQvHFm3qe-ZpAjUaznnyedymC26LbWowiAqmECAeTQQxFQXuO-UVumIL8=w1668-h1250-no)

4. __Sparkfun 9 DOF Razor IMU__ ![Razor](https://lh3.googleusercontent.com/k5Nw2gfF-WOnYy8LfWqGpVMo35Oo6TpXHRVXmAV95sAhXvfpBf-ZnLWXMkjdleLwuPQXWpkOJQPOQ6ZIiClDekwg2EGU6lQFVFtawdRG0eqfg1JihEmgRkY_zGV6LCKrMlUvR9DwJE7YxcVB4iFfrBGJyW_-cn9XsCfQHtXEoE550mJ_ADMquo5RJ3qCfxB3oHuyN1x0kMIQ0Di7S9Iwme7JMEIm4e9g0g5k7NFDQ-BTlPg4nUDv83MSpW3VqrMslRHmyWqTo3LJtsUqe3BuSHKOuvoHgbjYkHl_VSCccbiI8NzrGrnp6UbfyXbY3-3bgjOg4WDgs-I6imzuCz3NOJshhEPo-PBmomkD50ahz1MpI7FTkZDSbhzAT1rO82wxAq7tgrAkEPuIZKB9DuqX7no9tKoL7tdRDaDmXE9T27VAG3f_qpJdMwmfjXd5VbPp_50bMZ8ISuiA3KrRUXvJurYtpcROsBda9t1PCT3u1oi3mcQkIOyELYL1z5p2vlaAMk977Fl8lJn21GMmIAQP3mqmQg5WXnU09juhxRmG4Cx1a7o_Ja_w-zAg5PtsSBOKyVl2VMIArWzN6uKXTLuStRaajB5nmKBVyq4iBIUdEJE=w1668-h1250-no)

5. __SSD Drive__ ![I use the cheap one](https://lh3.googleusercontent.com/Xyaa6vtcwRNquh5iFCe4Nx0DTi5_nyvnwqWYvDOs6xzelHz4U0vF_mVxjNjTLcY6rz1XJOO-itoKRWY3tui6izZu8KahCnwZ-k8dqDdW9ttSF3YzVIvlhOvT7cGvSaFB1Lb__l_E8cURHwR1SFm_hUbMj4qpsD7vxRFmIMX8JFwyS45J-w8yuO9487sIn9vBti2SN8X0AoIhmVI_lv2_yx-2U9PcEhxMIKvccNhPnF5z1zTmMQ1WkKU0HCp_5xw-xJ6GUqdm4KVU0EpCIU5y0wm88kk-FPWgjABVf2W2XcK2mDanwRQ4D8VpX9agTKgV-LVdWGDW7kXJadDZQjl0Z5TJeksTXi60zHN7BibOohQbmYNT7aCqpKwdy2oRfaAc54kB7dfCoFLeGWZOwEp3CD2VW02ybTQ0bojX6WaWpmy6R6gX6_Fs5FkZfR9cbMYh1KJBPqFV_VPUymEiq5ybB1NKpFbSnC-FMHUnYxPASsbZmlv8EHPMCrJV_vgGoETenVbabwSB5XSjB4rylZnGGE7ReAVIPFGHED5nzsuPTwKr295zSrKIHqpRsneGta3J0B4d7IjwZC0a4AlLEJqU_AEtvW3vcfCt157ekKTToJw=w1668-h1250-no)

6. __Enertion FOCBOX VESC__ ![focbox](https://lh3.googleusercontent.com/cGhSnkrah5Z0Yrk07CFitAoKl9ObJDSl2Crx5RDWAh_t3cbn-Cp-p1cmnC01YWeZHpJ2LMOYozJH4iSn65mvD7a4bC_Nu_AdDMx20QjpBd-6ONUk9XBYMZy9nU32vBNWsi2BfFiFX10NpPnUlIMs-ZoBUW6mh98ML_FjIgRb-U_HRt3VGZePlAR4td7jpaztNwXg0cMJeFrpy3UhCQWUD1HEfQPpmZqKlL8ACMrFSc138d4PjW0ueoUTe0BkJOwGGBmGgu1oMdussAsY3E5forpUQL2ijEBEGgTjosC4qTtcuFTkjYEkE6aE6ssYp40UIvyWRLY7NBehcTIjDmQBcz807ohtpiqxHwyatsu5pim2hhZLkOuu6q4KUJsLknrHOhUS85FJ4emEX5MA0fNNm9OA2ZEaxlj3KOyeIuHbZm9_wv-47xE9vif8DAjMVVjjW6Umhy4DE0AttRbhhElRSHaBuCdhhsj7MYiN9yPhpXUXMPdiibnINO44fG1q0eS77POqjG5_ERM1TWjKOPRVSWVHC2pjC9Q5v1tto4eFVe04PCAdbrYLD_VgZLguCCibZ8B9xfwjvvOljlP1Kb3Iv8nHp9cilEiCa5FgWtU79cI=w1668-h1250-no)

7. __Traxxas RC Car__ ![Traxxas](https://lh3.googleusercontent.com/5i2UZIj6lF1DJvy-8yf2GHQcCL0lW-zxa9E-73uSmQ1Bgih7ReNLWU8gvtWznjNZc3qHyOVSIBsjPtwkVFrQ7V9ckrhoDjsYCGTYG9Z9piXTSljRVy-txbVBr3dX_gc1YL1lUU_Ci0sHy2uZ9Acd69NwqGXFVAaBNW8CTTwX03n_2EEh48k_KbXueVOisgR3_0Q6dziPcIMIAIaq1jpbEWq8oVrkRq-43IWFi-k1fZag-cZ-BcKCz7gkXx7ximmDVfS1jrdfvwQBK6fKlXuqMTAvnQSFx9a1ocU6-LiXPcn5ubA0AWFuLy6pPEhLOK5Fk3hG-BTbTstHIgwjywQRNMUg8_Dj5icwar8vQ-98u9o_PtMl0mqWHk8FkfNPjbm5cwmTWUEbSRFiMm0Et8wtGbQ3IPtt7tjfJvD_k0bMp_vWnDRKUYweh2jagxpX6EJ_k-GefibvvyPVvd3CSNxdiVb2-S-dFyW-d6sIn6oeaKBBPamvlpx0KEN7It3czKhgLIxuIXyzTm_-nmTYzhWbrEjnm-qau5q_M5-9Fx1b6HUaHBUjMcZ6zNQcrR2QGlFSwonW4UNZSoYzUE0JJiybQ0HnXApuf8OM2Dwsx0X5hyY=w1668-h1250-no)

# Getting Started
## Wire up your Jetson
* Ethernet cable from Jetson to router (same network as host pc)
* USB from Jetson to host pc
* HDMI cable from Jetson to your monitor
* Mouse and keyboard (you may need usb hub)

![wire up](https://lh3.googleusercontent.com/ZQM0WSnMpgsIoWimtF-QxXHnr6wdXQsp2YNTBL5Bw3BOr04u-7pzbTW2ECFbF9dUAZgRnoyXYuC7RRhMHEbwp-lDqhuDUIAmz-fpqBQB8xVaEzpvzdklDDTfA-9TkJpCYiBvBT0xEVD7gdTHEhiYjV1cr5UZicRXItQesT_tWGrDSWpsr53iWandfJ5WNk0gKIsb01tCwD186Wbmk4BK7XecN2S5q68ItKEQ49KgEie0yF4gIo_uuuAjd4q0TfKriFRvL76MK0FALidxtW0LtNTcpHrAno34KntjQOskdfyvEb2ymskwam-pOPWFKEzOq9-ZVgRo9tqITrAP1PXXr6qECnu-Rn0NCGksKRJ0PGxNd_0sP-wLuLW6dAEB384VMXjzEHGN55-Z8xD_ooCKFddo70dthh1lotdiwl7wEg7QQPjjiOFfDJqqaMOy3innRGOUGSFeH9P_pi3geW9ohMmrwEIlWODdY7sW0bfll7pLX6Pm_SG-8zZsqigmOLtOwCbyYk2oynqM0VNRd-4vs2dlVi0khcYzXWJ30FG54GK6MmpdsqYS7XtDQZa7yk6ogD_ISz0knSaLT42DGV_f6eHhvhWgkSShEOnrZIOSwDc=w1668-h1250-no)


## Step 1. Install Nvidia Jetpack on Host PC & Jetson TX1.
### In the end of this step you will be able to run CUDA examples on Jetson TX1.
![video](https://lh3.googleusercontent.com/6-EE7GCUbd_zza-2c_2OwihkmH0L6oQz4bHFaptoeedWok6fPlSYpTABGtx0J7-1IWWFAcfmNnOD7EAZEvnPdcwgYae3mnMoCoUj6LUIiHVjvY8YYLYDcGYzEcadK_DSpCooetOOETB_MN_CQ1w7Z9cwrv8Vn7RSpBl5xebIOMQk5wijETAp3e_EvGG1tdNB_punkOP4pP_F1eLKlR1BfhOWLgN3CaSlL96lGRNfZNwYTzO0NrlWNnhlSdiXR8MvqQ6own4uVU6CDbj6F-UdMkcOINSIQ2QNZ31irTqNNz0huBOlnYjpYuKHJshrB1SQXbRyjWwh7G4FFS4eHaSH75FSZUJ19kXIpY2dCxemjODbE1BmjAoV1IoNQEOAdp2nPNGrY3Fdjr_ltfWXP05OifUClhIpkjsrs-6xmpWQTZ9nBD7VJJQ28o7-OMIXaz63AUD3PV_N7Idtv8pXPsPR7Y1Pai9SAMDKrf8VpvYf8mGrnLneikS-ZxJW1qbRD28Z4YblmkD95vKGA69sdxJFk_Bvh-K9P4kPF5fxvcDgPcxFefaKDqfB4BnxaawQy9OzOBFdTnaAW3L8atv2_fRJcxigyBkQyHFESl87DMjibD8=w704-h1250-k-no) [See Video](https://photos.app.goo.gl/RfneNR6vpnrY4Q6m1)

1.1 Install virtual machine (ie. VirtualBox) running 64-bit Ubuntu 16.04 with at least 20 GB. You can skip this if you have Linux PC. 
Here is my setup ![virtualbox](assets/virtualbox.png)

1.2 Once logged in your newly installed Ubuntu, run 

```sudo apt-get update && sudo apt-get upgrade -y```

Tips: use fish shell for auto completion 

```sudo apt-get install fish -y```

Then you can activate fish shell instead of bash by typing ```fish```

*** If you use VirtualBox, don't forget to install Guest Additions in order to pass USB drive to the virtual machine.
![guest](assets/guest.png)

1.3 Download Jetpack from [Nvidia](https://developer.nvidia.com/embedded/jetpack).
(As of writing I'm on Jetpack 3.1)

1.4 CD into downloaed directory and change file permission to run the script.

```chmod 755 JetPack-L4T-3.1-linux-x64.run```

1.5 Run the downloaded file.

``` ./JetPack-L4T-3.1-linux-x64.run```

* __select your applicable platform and select packages (choose 'no action' for the host and 'install' for the Jetson__)

![select](assets/select.png)

![packages](assets/packages.png)

1.5 Once installing completed, Post Installation window shows up. The script will flash os onto your Jetson.

_You will need to put Jetson in Force USB Recovery mode_
* 1.5.1 Power off the Jetson (completely pull the plug)
* 1.5.2 Plug power cord back then press power button.
* 1.5.3 Press and hold 'Rec' button.
* 1.5.4 While pressing 'Rec' hit 'RST' button, let go and wait a few seconds then release 'Rec' button.
![buttons](https://lh3.googleusercontent.com/G8Ts-5WtoggEGScHnUXh38xwdanUTpc31T7reqynT9V_BB57bOP3CMUCL1v70-ob1EvvMQcyOvkH0zDZuV5uVORgDzzTW_-KmpH0smps3zo4qJ4-9XpX8wnItO823KSQDjx10uPDC2dUgMZfzmOiKJsxpZOTh5_d5ABztqLAG12RwJL4j0k307pqVWnmeSrwsEBqTMeg5LpsBYBOy9_5N908YKdhWB-gl5JLEzKAZP1S-Eg4dN49jW88o47JP-1WkE2BhI17OOVKb5TcddhEfSInurkLzwj-45hpSFi2vuJ3k_WJvKxEF3JN6Gt9GvTztx8hcDH0D6rX23g4muxP2v6CKLR5HoqAxuGVq7d82hJ7eAiEzXpk2wTHsO2SM75M5qYA3BD8Edz6nACVn2gj7FeVbjPsaLjbtW72vg_o9aSSe4yGR26hzBSOEjqpXY9UYmAavEkn_E9xW7K9BSkxB0dAphgJH1_3k42x2M7Op_D6piTQOlv6GTGn3U5Mq6SjyjZRKWFfg3n716MN479OvXqt0uLpUhWMBdWb8iWroy88MiRdNN81Mnt9jSl2CYV_Li06SV3Rhdg9DVpId87f58botKMnML_6acBiDrtceAE=w1668-h1250-no)

*** if you use VirtualBox, Click 'Devices' and select 'Nvidia'. ***

* 1.5.5 To verify if your virtual machine sees the NVidia, open up new termimal and type ```lsusb```.

* 1.5.6 Back to last termimal and hit 'Enter' to begin flashing.

![flashing](https://lh3.googleusercontent.com/QSHGLE8GlSZxd5oFEJRLwdg1o1bKgT0N9ym6dPGA7WsdPU3f9vJbjoKq8MVQsctmcHzkEKx5q8vBBop35ZKx7QuI4KANhpJjUK6FaG4sTBPqjL3IxXhKlVipkvYz4bXAwwwmWcsDUq7SI7ioRQwJ2YNHu1khjpcFwSDAH9WJFAMQFqX7mbNws9SsT_HV115x83H2kmJgiidIWJCxv9s14x4oYGfxCURRBD6nRd_WWNtcc8mKuh0hREisvcG6eYGgR0WJbWgfBxc1XrJtLxwzqIAEPTRFXtHXS3OKr44buSKXu7DGk8jUrnY-F9QlZzH96Me6EQOJAV3R9ZMnFM6DP_HdXnA0u2pfkGhruodrsDv0k-4Xs-nUGhrrrxbN_B3riL9aRdfItf7DApClcrvwEOcA5pugeyeglH00ilEEQvGSVoI-uEyX43RR_-iGKftCMo_gJw8iDp-DyU3SHBE8Dg6DesUGBwkbkXQ9Q-kj_-zirPuHRPx4xw6XaiSShkB9qQC4oOHnYA9N3Xx0E3tz7F34QEkoj472Nt6YPbz0u4H6cEX75RR61dPSMjAHv0VAEwdmv37-ogRz7YDgg7tRmcRH6Li_Nfdm6JVHlpwq4Uc=w1668-h1250-no)

1.6 You should see Ubuntu loading up on your HDMI monitor connected to the Jetson.
![done](https://lh3.googleusercontent.com/_zn6iAqNJu_pf5l8Bs_KceazqpVgDoPxavJr-ypgjw2JwqN-_XLSzPp8uK4wQY93-Z3KeIvEpwtgPaHPp4Y3eehWM1H3JRKLJYY9KDQC1f4IGFbo_BG3AWKiAG5ERKH-v78LYGRUHS0ibVvWUvDGxJ9VZoh6ifl05cuCCPvh1G9RkVAFBkqktQMaT685qbbREzymVaHyv68apd8CVlrzrlxX_ylOlEOKvsOgw-QVAr2eM9aAsAANydr9rgHqcpPYkHe-dFWMBBrdS58X5Fc0_OOLAl6oVZ98ACAPUVUcC77zoGV3S8dRET4FsOveL_p5DWcbI6QhbERfJoXV7HtlXyjXTaA8ar1o-jUGz0U9bwCqieVsXhIYus0171fvyp1OLCXQh-6IN5AslvvDusmVcv3SsdzF2xuA60Sq2hLgz0wLeYgTOQKlz3P0P8apGCvPefsgySXG210_u0LtUs2i3_AUTVvkEjBoLsIZvxf79oWdiWC2_4F6Y152JSOgv_YXEWV5wJ8YShHk4SzxoUFgNwDN6xxsleWeoD6CXVoKhishxTk1kUXUzDRPkSO2IUoMfWoK0GeffCzpARg6FlZR1gV8Z2i4lh4aOSg1sUF-hkY=w1668-h1250-no)

1.7 At host pc (or virtual machine), the installation script will have a hard time looking for the Jetson's ip address. Select option 2 to manually enter the ip of the Jetson. 
![ip](https://lh3.googleusercontent.com/Tw_Rvg1zBtz9Q7ad6lQTPYExABtOWX_XkrNAQHpMiU_JWiSPGEfqJsWsvhexzLwGQJadABrUmdeD1X521B0oXETpiyYfsUHWeQnsgP_T_C1tLZtrT53hzwSXnUJTRD10isav6xOCf3P_Mw-g6FCcX5d2o68mOd65O1Bva0BPeWY6xjv0vvStDwJuL6tBMzKS8oQ5otuk2Y0T_VCzYC0Ora7gT_iCNU3jna4Urw6CdMZYOszJ5a-TlqTgtfHX0BJzJX6QhRudz9GSDvVNfwt4dh2Vwugg8590w_chjq4BKEkFxEz9M0MO2BsvmW8OT5y8ad0bt99MnH_hP4mpmPx62uIcP_qAVFGcNlNl2E3CWLzguDx_BNW3cFfPy7KczTw5a7q6dTw0oSyvSIWaN7m0xsX-Uvrp9mSRNpkkJ7OzEs7x4AgN4_5Iu3v0DZu4mudwYrO0D-27YW6pjGJgPs6ucT2PwdQCrHGrHZghlVs1K9rXRMg0D5_pZGNQdpgeIvsPnxA_2WDC_wNpPVC1dsyzoqNRPxejWFp2PmFwAotSzL0YJNbV8qqckE1xpQjxZIOf0gBjuxLzU6U1mHBdisg2z5q1llz8g9RHJanw4A_-8O4=w1668-h1250-no)


1.8 You can grab the ip of the Jetson by heading over to Jetson and type 'ifconfig' or click the network icon on the top-right corner.
![as](https://lh3.googleusercontent.com/Gmu6n74E7lemyt3_qPdFN3NLEITMHEQirbrN-y75fxwCnSR6BkZyHHtQZ-PYT1PHvyLEImoKYQyiFqzwyVIhWKwvnDEmWHnLaxGNLsVP07Z0vDCJezKtLtNxVcVUCPXRahdhglae1fVj5VhRkfxS3uy3BHuV0bhrivc-1_dt1dbfMrLQvrNILpTGELYso24NRyr7gxMDDLjyEkLDteEvAvQcEg0-3jsVPLv-1vUneHBmkEcpAvoIinEKnwD9q6rZaI15He-DLklnc-af2fcQmmUzHfOpq2yohKwqmZyWyuIIa9DUPyfItEcMzyUE7n8l-6zz5r88j4vYcZJLKK-Uk688rYQFY_5pfKmrbLbNDe1y-hP86s1URML3xY94-b89Tr8N1oNf1bC-Arwy6Y_Pi-4EEZNr3YzP-niWW1ipYqFstSLbxL6UfQWeYkcZInmDTpwVGabX8Z0NVNL_-JzZnLaguOz9wofTDyAWniooZxua-sb7ZeeQ1x5xIkC5ZJzPQ_826OSu2rDHAqMdFI4gCEKZSO6qCGJpleYqjxJpKV2gKCh7Nt1Lx-PU3wMH63QxV-uc0Q5fDnbGsWO_PnyjpkMJ10I2hqvYinse2i9a7ec=w1668-h1250-no)

1.9 Enter the IP and username & password in the dialog box shown on the host pc.

Device IP Address: ```your ip```
Username: ```nvidia```
Password: ```nvidia```

*** just to confirm the process can access the device, you can try ssh into the Jetson using this info first ```ssh nvidia@192.168.1.99``` ***

if all goes well, hit enter.

1.10 Once finished, you can click _Remove downloaed files._


### __INSTALL CUDA 8.0 ON JETSON__

1.11 Now go to Jetson, and

```cd ~/cuda-l4t```

```cuda-l4t.sh cuda-repo-l4t-8-0-local_8.0.84-1_arm64.deb 8.0 8.0```

Then reload .bashrc since the script will add binaries to it.

```source ~/.bashrc```


now check if CUDA 8.0 is installed.

```nvcc -V```

To test it, run some sample files.

```cd ~/NVIDIA_CUDA-8.0_Samples/bin/aarch64/linux/release```

```./particles``` or anything else.
[See Video](https://photos.app.goo.gl/RfneNR6vpnrY4Q6m1)
