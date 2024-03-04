#include <bits/stdc++.h>
using namespace std;

using Vec2 = array<double, 2>;
using Vec3 = array<double, 3>;
using Matrix = vector<vector<double>>;

// ---------------- Coordinate system ----------------

// Translate point relative to camera
Vec3 translate(const Vec3& point, const Vec3& camera_position) {
    return { point[0] - camera_position[0],
             point[1] - camera_position[1],
             point[2] - camera_position[2] };
}

// ---------------- Projection functions ----------------

Vec2 convert_result(double x, double y, double s_width, double s_height) {
    // Takes a center-origin coordinate and maps it back to top-left origin
    return { x + s_width/2.0, y + s_height/2.0 };
}

Vec2 efficient_perspective_projection(const Vec3& translated_point,
                                      double screen_width, double screen_height) {
    double d = 400.0;
    return convert_result(d * translated_point[0] / translated_point[2],
                          d * translated_point[1] / translated_point[2],
                          screen_width,
                          screen_height);
}

array<Vec2, 3> efficient_triangle_projection(const array<Vec3, 3>& tri,
                                             double screen_width, double screen_height) {
    return { efficient_perspective_projection(tri[0], screen_width, screen_height),
             efficient_perspective_projection(tri[1], screen_width, screen_height),
             efficient_perspective_projection(tri[2], screen_width, screen_height) };
}

Vec2 project_3d_point_to_2d(const Vec3& point,
                            double screen_width, double screen_height,
                            const Vec3& camera_position,
                            bool orthogonal=false) {
    if (orthogonal) {
        return convert_result(point[0], point[1], screen_width, screen_height);
    }

    Vec3 t = translate(point, camera_position);

    double d = 500.0;
    return convert_result(d * t[0] / t[2],
                          d * t[1] / t[2],
                          screen_width,
                          screen_height);
}

array<Vec2, 3> project_triangle(const Vec3& v1, const Vec3& v2, const Vec3& v3,
                                double screen_width, double screen_height,
                                const Vec3& camera_position) {
    return { project_3d_point_to_2d(v1, screen_width, screen_height, camera_position),
             project_3d_point_to_2d(v2, screen_width, screen_height, camera_position),
             project_3d_point_to_2d(v3, screen_width, screen_height, camera_position) };
}

// ---------------- Matrix multiplication ----------------

Matrix matrix_multiplication(const Matrix& m1, const Matrix& m2) {
    int rows1 = m1.size();
    int cols1 = m1[0].size();
    int rows2 = m2.size();
    int cols2 = m2[0].size();

    if (cols1 != rows2) {
        throw invalid_argument("It is not possible to multiply these matrices.");
    }

    Matrix result(rows1, vector<double>(cols2, 0.0));

    for (int i = 0; i < rows1; i++) {
        for (int j = 0; j < cols2; j++) {
            for (int w = 0; w < rows2; w++) {
                result[i][j] += m1[i][w] * m2[w][j];
            }
        }
    }

    return result;
}

// ---------------- Example usage ----------------

int main() {
    Vec3 point = {1.0, 2.0, 5.0};
    Vec3 camera = {0.0, 0.0, 0.0};

    Vec2 projected = project_3d_point_to_2d(point, 800, 600, camera);
    cout << "Projected point: (" << projected[0] << ", " << projected[1] << ")\n";

    Matrix m1 = {{1, 2}, {3, 4}};
    Matrix m2 = {{5, 6}, {7, 8}};
    Matrix res = matrix_multiplication(m1, m2);

    cout << "Matrix multiplication result:\n";
    for (auto& row : res) {
        for (auto& val : row) cout << val << " ";
        cout << "\n";
    }
}
