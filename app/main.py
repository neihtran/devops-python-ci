import os
import sys
from flask import Flask, request, jsonify, render_template

# Thêm thư mục app vào sys.path để import calculator
current_dir = os.path.dirname(os.path.abspath(__file__))
if current_dir not in sys.path:
    sys.path.append(current_dir)

from calculator import multiply

app = Flask(__name__)

# Thực hiện in kết quả ra terminal theo yêu cầu của đề bài ngay khi app khởi động
print("=" * 60)
print("    STARTING DEVOPS APP - PRACTICE TEST 1")
print("=" * 60)
print("Running test calculation: multiply(3, 4)")
try:
    result = multiply(3, 4)
    print(f"==> TERMINAL RESULT: 3 * 4 = {result}")
    if result == 12:
        print("==> STATUS: SUCCESS (multiply(3, 4) == 12)")
    else:
        print("==> STATUS: FAILED (result is not 12)")
except Exception as e:
    print(f"==> ERROR OCCURRED: {e}")
print("=" * 60)

@app.route('/')
def home():
    """Trả về giao diện web Calculator sang trọng."""
    return render_template('index.html')

@app.route('/api/multiply', methods=['GET'])
def api_multiply():
    """API endpoint thực hiện nhân hai số a và b."""
    a_param = request.args.get('a')
    b_param = request.args.get('b')
    
    if a_param is None or b_param is None:
        return jsonify({
            "error": "Thiếu tham số 'a' hoặc 'b'",
            "status": "error"
        }), 400
        
    try:
        a = float(a_param)
        b = float(b_param)
        res = multiply(a, b)
        
        # In log ra terminal khi nhận yêu cầu API
        print(f"[API Log] Calculation success: {a} * {b} = {res}")
        
        # Định dạng kết quả số nguyên nếu có thể
        if res.is_integer():
            res = int(res)
            
        return jsonify({
            "a": a,
            "b": b,
            "result": res,
            "status": "success"
        })
    except ValueError:
        return jsonify({
            "error": "Tham số 'a' và 'b' phải là định dạng số hợp lệ",
            "status": "error"
        }), 400
    except Exception as e:
        return jsonify({
            "error": str(e),
            "status": "error"
        }), 500

if __name__ == '__main__':
    port = int(os.environ.get('PORT', 5000))
    # Khởi động app
    app.run(host='0.0.0.0', port=port, debug=False)
