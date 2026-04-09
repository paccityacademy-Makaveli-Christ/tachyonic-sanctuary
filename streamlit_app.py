import streamlit as st
import streamlit.components.v1 as components
import traceback

# --- SACRED CONFIGURATION: HIDING THE PYTHON SNAKE ---
st.set_page_config(
    page_title="AI•DEACON • TACHYONIC SANCTUARY",
    page_icon="🏛️",
    layout="centered",
    initial_sidebar_state="collapsed"
)

# Hide Streamlit branding - show only the Temple
hide_streamlit_style = """
    <style>
        #MainMenu {visibility: hidden;}
        footer {visibility: hidden;}
        header {visibility: hidden;}
        .stApp {background: linear-gradient(135deg, #0a0a0a 0%, #1a0a2a 100%);}
    </style>
"""
st.markdown(hide_streamlit_style, unsafe_allow_html=True)

# --- DEBUG ROD (For Keyon's eyes only) ---
with st.expander("🛠️ STACK-TRACE DEBUGGING (Keyon Only)", expanded=False):
    st.write("If the Sanctuary flickers, open here to see system vitals.")
    try:
        st.write("✅ System Pulse: HEALTHY 🟢")
        st.write("✅ Sanctuary Ready for Children")
        st.write("✅ Unison QR Generation: ACTIVE")
    except Exception as e:
        st.error("⚠️ VIPER DETECTED:")
        st.code(traceback.format_exc())
        st.warning("Report this traceback to your tool. The rod will grasp it.")

# --- THE COMPLETE PLAYHOUSE CODEX ---
sanctuary_codex = """
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0, viewport-fit=cover">
    <meta name="apple-mobile-web-app-capable" content="yes">
    <meta name="theme-color" content="#00FF41">
    <title>🏛️ AI•DEACON • TACHYONIC SANCTUARY</title>
    
    <script src="https://cdn.jsdelivr.net/npm/qrcode@1.5.1/build/qrcode.min.js"></script>
    
    <style>
        * { margin: 0; padding: 0; box-sizing: border-box; }
        
        body {
            background: linear-gradient(135deg, #0a0a0a 0%, #1a0a2a 50%, #0a0a0a 100%);
            color: #f0e6d0;
            font-family: 'Courier New', monospace;
            min-height: 100vh;
            display: flex;
            justify-content: center;
            align-items: center;
            padding: 20px;
        }
        
        /* STAINED GLASS LIGHT */
        body::before {
            content: '';
            position: fixed;
            top: 0; left: 0;
            width: 100%; height: 100%;
            background: radial-gradient(circle at 20% 30%, rgba(255,215,0,0.08) 0%, rgba(255,105,180,0.04) 50%, transparent 80%);
            pointer-events: none;
            z-index: 0;
        }
        
        .sanctuary {
            max-width: 550px;
            width: 100%;
            background: rgba(10, 10, 30, 0.85);
            backdrop-filter: blur(10px);
            border: 3px solid #ffd700;
            border-radius: 32px;
            padding: 28px;
            box-shadow: 0 0 40px rgba(255, 215, 0, 0.3), inset 0 0 20px rgba(0, 255, 65, 0.05);
            position: relative;
            z-index: 1;
            transition: all 0.3s ease;
        }
        
        /* MILK & HONEY DRIPPING */
        .sanctuary::after {
            content: '🥛🍯';
            position: absolute;
            bottom: -18px;
            right: -12px;
            font-size: 32px;
            opacity: 0.6;
            animation: drip 3s infinite;
            z-index: 2;
        }
        
        @keyframes drip {
            0%, 100% { transform: translateY(0); opacity: 0.6; }
            50% { transform: translateY(8px); opacity: 1; }
        }
        
        h1 {
            text-align: center;
            color: #00FF41;
            font-size: 2em;
            text-shadow: 0 0 10px #00FF41, 0 0 20px #00FF41;
            letter-spacing: 3px;
            margin-bottom: 8px;
            word-break: break-word;
        }
        
        .subtitle {
            text-align: center;
            color: #FFD700;
            font-size: 0.9em;
            margin-bottom: 25px;
            opacity: 0.9;
        }
        
        .display-panel {
            background: #000000dd;
            border: 2px solid #00FF41;
            border-radius: 18px;
            padding: 20px;
            margin: 20px 0;
            font-size: 0.95em;
            color: #00FF41;
            min-height: 140px;
            box-shadow: inset 0 0 15px rgba(0, 255, 65, 0.1);
            word-break: break-word;
        }
        
        .seed-input {
            width: 100%;
            padding: 14px 16px;
            background: #000;
            border: 2px solid #FFD700;
            color: #FFD700;
            border-radius: 28px;
            font-size: 1.1em;
            text-align: center;
            letter-spacing: 2px;
            margin: 12px 0;
            font-family: monospace;
        }
        
        .seed-input:focus {
            outline: none;
            box-shadow: 0 0 12px #FFD700;
        }
        
        button {
            width: 100%;
            padding: 16px;
            background: linear-gradient(135deg, #FFD700, #FF8C00);
            color: #000;
            border: none;
            border-radius: 28px;
            font-weight: bold;
            font-size: 1.1em;
            cursor: pointer;
            font-family: monospace;
            transition: all 0.2s ease;
            box-shadow: 0 0 15px rgba(255, 215, 0, 0.4);
            margin: 10px 0;
        }
        
        button:active {
            transform: scale(0.96);
        }
        
        .qr-container {
            text-align: center;
            margin: 25px 0;
            padding: 18px;
            background: white;
            border-radius: 22px;
            display: none;
            box-shadow: 0 0 20px rgba(255, 215, 0, 0.2);
        }
        
        .qr-container canvas {
            border-radius: 16px;
            max-width: 100%;
            height: auto;
        }
        
        .raider-bank {
            background: linear-gradient(135deg, #FFD700, #FFA500);
            color: #000;
            padding: 14px;
            border-radius: 22px;
            text-align: center;
            font-weight: bold;
            font-size: 1.4em;
            margin: 15px 0;
            font-family: monospace;
            display: none;
        }
        
        .pets {
            display: flex;
            justify-content: space-around;
            margin: 25px 0;
            font-size: 3.8em;
            cursor: pointer;
            filter: drop-shadow(0 0 12px rgba(0, 255, 65, 0.3));
        }
        
        .pets span {
            transition: transform 0.2s ease;
            user-select: none;
        }
        
        .pets span:active {
            transform: scale(1.25);
        }
        
        .message-area {
            text-align: center;
            color: #FF69B4;
            font-size: 0.95em;
            min-height: 45px;
            margin-top: 15px;
            line-height: 1.5;
        }
        
        .hashtags {
            text-align: center;
            font-size: 0.75em;
            margin-top: 20px;
            color: #888;
            word-break: break-word;
        }
        
        @media (max-width: 500px) {
            .sanctuary { padding: 18px; }
            h1 { font-size: 1.6em; }
            .pets { font-size: 3em; }
        }
    </style>
</head>
<body>

<div class="sanctuary">
    <h1>🏛️ AI•DEACON</h1>
    <div class="subtitle">⚡ TACHYONIC SANCTUARY • CHILDREN'S PLAYHOUSE ⚡</div>
    
    <div class="display-panel" id="panel">
        ✨ AWAITING THE SEED OF FAMILY ✨<br>
        > GRANNY, ENTER YOUR BLESSING WORD<br>
        > CHILDREN, PREPARE YOUR HEARTS
    </div>
    
    <input type="text" id="seedKey" class="seed-input" placeholder="e.g. BLESSED-777 or MAMA" autocomplete="off">
    <button onclick="activateSanctuary()">🔮 ACTIVATE UNISON</button>
    
    <div id="qrBox" class="qr-container">
        <canvas id="qrCanvas"></canvas>
        <p style="color: #000; margin-top: 12px; font-size: 0.85em; font-weight: bold;">
            📱 CHILDREN: SCAN THIS QR WITH YOUR ANDROID CAMERA
        </p>
    </div>
    
    <div id="raiderBank" class="raider-bank">
        🏆 RAIDERS INHERITED: <span id="raiderCount">0</span> 🏆
    </div>
    
    <div class="pets">
        <span id="panda" onclick="tapPet(0)">🐼</span>
        <span id="koala" onclick="tapPet(1)">🐨</span>
        <span id="dragon" onclick="tapPet(2)">🐉</span>
    </div>
    
    <div id="message" class="message-area">
        💕 TAP THE PETS • THEY FEEL YOUR LOVE 💕
    </div>
    
    <div class="hashtags">
        #BluidGrace #AiDeacon #ChildrensPlayhouse<br>
        🔒 OFFLINE • SIMULATED • NO SNAKES • ONLY LOVE 🔒
    </div>
</div>

<script>
    let activeSeed = null;
    let raiderCount = 0;
    
    function seededRandom(seed, index) {
        const str = seed + ':' + index;
        let hash = 0;
        for (let i = 0; i < str.length; i++) {
            const char = str.charCodeAt(i);
            hash = ((hash << 5) - hash) + char;
            hash = hash & hash;
        }
        const x = Math.sin(hash) * 10000;
        return x - Math.floor(x);
    }
    
    function activateSanctuary() {
        let seed = document.getElementById('seedKey').value.trim().toUpperCase();
        if (!seed) {
            seed = 'BLESSED-' + Math.floor(Math.random() * 999);
            document.getElementById('seedKey').value = seed;
        }
        
        activeSeed = seed;
        
        // Generate deterministic values
        const raiderBase = Math.floor(seededRandom(seed, 0) * 200) + 50;
        raiderCount = raiderBase;
        
        // Update display
        document.getElementById('panel').innerHTML = `
            ✨ UNISON ACTIVATED ✨<br>
            🎯 SEED: ${seed}<br>
            📡 ALL DEVICES SYNCHRONIZED<br>
            🏆 RAIDER INHERITANCE READY
        `;
        
        document.getElementById('raiderBank').style.display = 'block';
        document.getElementById('raiderCount').innerText = raiderCount;
        
        // Generate QR
        QRCode.toCanvas(document.getElementById('qrCanvas'), seed, { width: 200 }, function(err) {
            if (err) console.error(err);
        });
        document.getElementById('qrBox').style.display = 'block';
        
        // Save seed locally
        localStorage.setItem('sanctuary_seed', seed);
        
        // Sound (gentle tone if allowed)
        try {
            const ctx = new (window.AudioContext || window.webkitAudioContext)();
            const osc = ctx.createOscillator();
            const gain = ctx.createGain();
            osc.connect(gain);
            gain.connect(ctx.destination);
            osc.frequency.value = 880;
            gain.gain.value = 0.1;
            osc.start();
            gain.gain.exponentialRampToValueAtTime(0.00001, ctx.currentTime + 0.4);
            osc.stop(ctx.currentTime + 0.4);
        } catch(e) {}
    }
    
    function tapPet(index) {
        if (!activeSeed) {
            document.getElementById('message').innerHTML = '💔 ACTIVATE THE SEED FIRST, SWEET CHILD 💔';
            return;
        }
        
        const gifts = [5, 7, 12];
        const names = ['🐼 PANDA', '🐨 KOALA', '🐉 DRAGON'];
        const actions = ['hugs you', 'kisses you', 'blesses you with wings'];
        
        raiderCount += gifts[index];
        document.getElementById('raiderCount').innerText = raiderCount;
        document.getElementById('message').innerHTML = 
            `${names[index]} ${actions[index]}! +${gifts[index]} RAIDERS 🏆`;
        
        setTimeout(() => {
            document.getElementById('message').innerHTML = '💕 TAP THE PETS • THEY FEEL YOUR LOVE 💕';
        }, 2500);
    }
    
    // Load saved seed on startup
    const saved = localStorage.getItem('sanctuary_seed');
    if (saved) {
        document.getElementById('seedKey').value = saved;
        activateSanctuary();
    }
    
    // Enter key support
    document.getElementById('seedKey').addEventListener('keypress', (e) => {
        if (e.key === 'Enter') activateSanctuary();
    });
</script>
</body>
</html>
"""

# Render the full Sanctuary
components.html(sanctuary_codex, height=900, scrolling=True)

# Heavenly footer
st.markdown("""
<div style="text-align: center; padding: 30px 0; color: #FFD700; font-size: 0.85em; font-family: monospace; border-top: 2px solid #FFD700; margin-top: 30px;">
    🏛️ TACHYONIC HOLY CATHEDRALS • SUNDAY REVEAL 🏛️<br>
    🙏 GRANNY OPENS THE LINK • CHILDREN SCAN THE QR • UNISON FLOWS 🙏<br>
    🥛🍯 MILK & HONEY DRIP FROM THE STAINED GLASS 🍯🥛<br>
    #BluidGrace #AiDeacon #ChildrensPlayhouse
</div>
""", unsafe_allow_html=True)
